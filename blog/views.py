from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import Post, PostCategory, Tag
from core.models import SiteSettings

POSTS_PER_PAGE = 9


def blog_list(request):
    qs = (
        Post.objects
        .filter(status='published')
        .select_related('category')
        .prefetch_related('tags')
    )
    categories = PostCategory.objects.all()

    active_cat_slug = request.GET.get('kategoria', '')
    active_tag_slug = request.GET.get('tag', '')
    search_q        = request.GET.get('q', '').strip()

    if active_cat_slug:
        qs = qs.filter(category__slug=active_cat_slug)
    if active_tag_slug:
        qs = qs.filter(tags__slug=active_tag_slug)
    if search_q:
        qs = qs.filter(
            Q(title__icontains=search_q) |
            Q(excerpt__icontains=search_q) |
            Q(author__icontains=search_q)
        )

    total = qs.count()

    paginator = Paginator(qs, POSTS_PER_PAGE)
    page_number = request.GET.get('strona', 1)
    try:
        posts = paginator.page(page_number)
    except (EmptyPage, PageNotAnInteger):
        posts = paginator.page(1)

    active_category = categories.filter(slug=active_cat_slug).first() if active_cat_slug else None
    active_tag      = Tag.objects.filter(slug=active_tag_slug).first() if active_tag_slug else None

    return render(request, 'blog/blog_list.html', {
        'posts':           posts,
        'categories':      categories,
        'active_cat_slug': active_cat_slug,
        'active_category': active_category,
        'active_tag_slug': active_tag_slug,
        'active_tag':      active_tag,
        'search_q':        search_q,
        'total':           total,
        'site_settings':   SiteSettings.get(),
    })


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')

    related_qs = Post.objects.filter(status='published').exclude(pk=post.pk)
    if post.category:
        related_qs = related_qs.filter(category=post.category)
    related = related_qs.select_related('category')[:3]

    return render(request, 'blog/blog_detail.html', {
        'post':          post,
        'related':       related,
        'site_settings': SiteSettings.get(),
    })
