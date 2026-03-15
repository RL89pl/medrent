from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.db.models import Q
from .models import Product, Category, SiteSettings, ContactMessage


def _build_category_groups(qs):
    """Return list of (category, [(subcategory, [products])]) for template."""
    groups = []
    for cat in Category.objects.prefetch_related('products').all():
        products = list(qs.filter(category=cat))
        if not products:
            continue
        # Group by subcategory (preserving order)
        sub_groups = {}
        for p in products:
            key = p.subcategory or ''
            sub_groups.setdefault(key, []).append(p)
        groups.append((cat, list(sub_groups.items())))
    return groups


def home(request):
    categories = Category.objects.all()
    settings = SiteSettings.get()
    return render(request, 'core/index.html', {
        'categories': categories,
        'site_settings': settings,
    })


def oferta(request):
    qs = Product.objects.filter(is_active=True).select_related('category')
    categories = Category.objects.all()

    active_slug = request.GET.get('kategoria', '')
    search_q = request.GET.get('q', '').strip()

    if active_slug:
        qs = qs.filter(category__slug=active_slug)
    if search_q:
        qs = qs.filter(
            Q(name__icontains=search_q) |
            Q(short_description__icontains=search_q) |
            Q(subcategory__icontains=search_q)
        )

    category_groups = _build_category_groups(qs)
    active_category = categories.filter(slug=active_slug).first() if active_slug else None

    return render(request, 'core/oferta.html', {
        'category_groups': category_groups,
        'categories': categories,
        'active_slug': active_slug,
        'active_category': active_category,
        'search_q': search_q,
        'total': qs.count(),
        'site_settings': SiteSettings.get(),
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    related = (
        Product.objects
        .filter(category=product.category, is_active=True)
        .exclude(pk=product.pk)[:4]
    )

    sent = False
    errors = {}

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        message = request.POST.get('message', '').strip()

        if not name:
            errors['name'] = 'Podaj imię i nazwisko.'
        if not email or '@' not in email:
            errors['email'] = 'Podaj poprawny adres email.'
        if not message:
            errors['message'] = 'Wpisz wiadomość.'

        if not errors:
            ContactMessage.objects.create(
                product=product,
                name=name, email=email, phone=phone, message=message,
            )
            sent = True

    return render(request, 'core/product_detail.html', {
        'product': product,
        'related': related,
        'sent': sent,
        'errors': errors,
        'post': request.POST,
        'site_settings': SiteSettings.get(),
    })


def search_ajax(request):
    q = request.GET.get('q', '').strip()
    if len(q) < 2:
        return JsonResponse({'results': [], 'total': 0})

    qs = Product.objects.filter(is_active=True).filter(
        Q(name__icontains=q) |
        Q(short_description__icontains=q) |
        Q(subcategory__icontains=q) |
        Q(category__name__icontains=q)
    ).select_related('category')

    total = qs.count()
    results = []
    for p in qs[:6]:
        results.append({
            'name': p.name,
            'url': p.get_absolute_url(),
            'category': p.category.name,
            'short_description': p.short_description[:80] if p.short_description else '',
            'image': p.image.url if p.image else None,
        })

    return JsonResponse({'results': results, 'total': total})
