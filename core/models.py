from django.db import models
from django.utils.text import slugify
from .utils import compress_image


class ContactMessage(models.Model):
    product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL,
        null=True, blank=True, related_name='inquiries',
        verbose_name='Produkt'
    )
    name = models.CharField(max_length=120, verbose_name='Imię i nazwisko')
    email = models.EmailField(verbose_name='Email')
    phone = models.CharField(max_length=30, blank=True, verbose_name='Telefon')
    message = models.TextField(verbose_name='Wiadomość')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Wiadomość'
        verbose_name_plural = 'Wiadomości'

    def __str__(self):
        product_name = self.product.name if self.product else 'ogólne'
        return f"{self.name} – {product_name} ({self.created_at.strftime('%d.%m.%Y')})"


class SiteSettings(models.Model):
    # ── LOGO / MARKA ─────────────────────────────────────────────────────────
    logo    = models.ImageField(upload_to='logo/',    blank=True, null=True, verbose_name='Logo firmy',
                                help_text='Wyświetlane w nagłówku i stopce. Zalecana wysokość: 40–60 px.')
    favicon = models.ImageField(upload_to='favicon/', blank=True, null=True, verbose_name='Favicon',
                                help_text='Ikona zakładki przeglądarki. Zalecany rozmiar: 32×32 lub 64×64 px (PNG/ICO).')

    # ── SEO ───────────────────────────────────────────────────────────────────
    meta_description = models.CharField(
        max_length=300, blank=True,
        verbose_name='Meta description (strona główna)',
        help_text='Opis strony widoczny w wynikach wyszukiwarki. Maks. 160 znaków.'
    )
    og_image = models.ImageField(
        upload_to='og/', blank=True, null=True,
        verbose_name='OG Image (udostępnianie)',
        help_text='Grafika widoczna przy udostępnianiu strony w social media. Zalecany rozmiar: 1200×630 px.'
    )

    # ── HERO ─────────────────────────────────────────────────────────────────
    hero_image    = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Zdjęcie tła')
    hero_eyebrow  = models.CharField(max_length=60,  default='LUMA',              verbose_name='Tekst nad tytułem')
    hero_title1   = models.CharField(max_length=80,  default='Wypożyczalnia',     verbose_name='Tytuł – linia 1')
    hero_title2   = models.CharField(max_length=80,  default='Medyczna',          verbose_name='Tytuł – linia 2')
    hero_subtitle = models.CharField(max_length=220, default='Profesjonalny sprzęt rehabilitacyjny – wypożycz, kup lub zamów z dostawą', verbose_name='Podtytuł')

    # ── USŁUGI (3 kafelki) ───────────────────────────────────────────────────
    service1_title = models.CharField(max_length=80,  default='Wypożycz',                                                   verbose_name='Usługa 1 – tytuł')
    service1_desc  = models.CharField(max_length=200, default='Szeroki wybór sprzętu rehabilitacyjnego na dni, tygodnie lub miesiące', verbose_name='Usługa 1 – opis')
    service2_title = models.CharField(max_length=80,  default='Kup na własność',                                            verbose_name='Usługa 2 – tytuł')
    service2_desc  = models.CharField(max_length=200, default='Sprawdzony sprzęt w atrakcyjnych cenach – nowy i używany',  verbose_name='Usługa 2 – opis')
    service3_title = models.CharField(max_length=80,  default='Zamów dostawę',                                              verbose_name='Usługa 3 – tytuł')
    service3_desc  = models.CharField(max_length=200, default='Przywozimy sprzęt pod Twoje drzwi – szybko i wygodnie',    verbose_name='Usługa 3 – opis')

    # ── O NAS ────────────────────────────────────────────────────────────────
    about_tag   = models.CharField(max_length=60,  default='O nas',                               verbose_name='O nas – etykieta')
    about_title = models.CharField(max_length=200, default='Jesteśmy z Tobą, gdy zdrowie tego wymaga.', verbose_name='O nas – tytuł')
    about_lead  = models.CharField(max_length=300, default='Od lat pomagamy pacjentom i ich rodzinom w powrocie do sprawności.', verbose_name='O nas – lead')
    about_body  = models.TextField(default='Nasza wypożyczalnia sprzętu rehabilitacyjnego powstała z prostej potrzeby – każdy zasługuje na wygodny dostęp do profesjonalnego sprzętu, bez zbędnych formalności i w przystępnej cenie. Oferujemy indywidualne podejście do każdego klienta i doradzimy w wyborze odpowiedniego sprzętu.', verbose_name='O nas – treść')
    about_check_items = models.JSONField(
        default=list, blank=True,
        verbose_name='O nas – lista cech',
        help_text='Lista punktów, np. ["Wieloletnie doświadczenie", "Konkurencyjne ceny"]'
    )
    about_stat1_number = models.CharField(max_length=20, default='500+', verbose_name='Statystyka 1 – liczba')
    about_stat1_label  = models.CharField(max_length=60, default='Zadowolonych klientów', verbose_name='Statystyka 1 – opis')
    about_stat2_number = models.CharField(max_length=20, default='100+', verbose_name='Statystyka 2 – liczba')
    about_stat2_label  = models.CharField(max_length=60, default='Modeli sprzętu', verbose_name='Statystyka 2 – opis')
    about_image = models.ImageField(upload_to='about/', blank=True, null=True, verbose_name='O nas – zdjęcie')

    # ── KONTAKT ───────────────────────────────────────────────────────────────
    contact_phone        = models.CharField(max_length=30,  default='+48 000 000 000',       verbose_name='Telefon')
    contact_phone_hours  = models.CharField(max_length=60,  default='Pon–Pt: 8:00–18:00',   verbose_name='Godziny telefoniczne')
    contact_email        = models.EmailField(               default='kontakt@luma.pl',       verbose_name='Email')
    contact_email_note   = models.CharField(max_length=60,  default='Odpowiadamy w 24h',    verbose_name='Nota przy emailu')
    contact_address      = models.CharField(max_length=200, blank=True,                     verbose_name='Adres')
    contact_address_note = models.CharField(max_length=60,  default='Zapraszamy do siedziby', verbose_name='Nota przy adresie')

    class Meta:
        verbose_name = 'Ustawienia strony'
        verbose_name_plural = 'Ustawienia strony'

    def __str__(self):
        return 'Ustawienia strony'

    def save(self, *args, **kwargs):
        self.pk = 1
        # Track which images are new/changed before saving
        changed_images = []
        if self.logo and self.logo.name:
            old = SiteSettings.objects.filter(pk=1).values_list('logo', flat=True).first()
            if old != self.logo.name:
                changed_images.append('logo')
        if self.favicon and self.favicon.name:
            old = SiteSettings.objects.filter(pk=1).values_list('favicon', flat=True).first()
            if old != self.favicon.name:
                changed_images.append('favicon')
        if self.og_image and self.og_image.name:
            old = SiteSettings.objects.filter(pk=1).values_list('og_image', flat=True).first()
            if old != self.og_image.name:
                changed_images.append('og_image')
        if self.hero_image and self.hero_image.name:
            old = SiteSettings.objects.filter(pk=1).values_list('hero_image', flat=True).first()
            if old != self.hero_image.name:
                changed_images.append('hero_image')
        if self.about_image and self.about_image.name:
            old = SiteSettings.objects.filter(pk=1).values_list('about_image', flat=True).first()
            if old != self.about_image.name:
                changed_images.append('about_image')
        super().save(*args, **kwargs)
        for field_name in changed_images:
            compress_image(getattr(self, field_name))

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    icon_key = models.CharField(max_length=40, default='default')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Kategoria'
        verbose_name_plural = 'Kategorie'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    subcategory = models.CharField(max_length=120, blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    long_description = models.TextField(blank=True)
    max_load = models.CharField(max_length=30, blank=True)
    warranty_years = models.PositiveSmallIntegerField(default=0)
    ce_certified = models.BooleanField(default=True)
    for_rent = models.BooleanField(default=True)
    for_sale = models.BooleanField(default=True)
    specs = models.JSONField(default=list, blank=True)   # [{"label": "Zasięg", "value": "≤20 km"}, ...]
    features = models.JSONField(default=list, blank=True) # ["Składany", "Lekki", ...]
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Zdjęcie')
    badge = models.CharField(max_length=60, blank=True)   # np. "5 lat gwarancji"
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['category__order', 'order', 'name']
        verbose_name = 'Produkt'
        verbose_name_plural = 'Produkty'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name)
            slug = base
            i = 1
            while Product.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{i}'
                i += 1
            self.slug = slug
        _compress = False
        if self.image and self.image.name:
            old = Product.objects.filter(pk=self.pk).values_list('image', flat=True).first() if self.pk else None
            _compress = old != self.image.name
        super().save(*args, **kwargs)
        if _compress:
            compress_image(self.image)

    def __str__(self):
        return self.name

    def get_specs_list(self):
        """Return specs suitable for the detail template."""
        return self.specs if isinstance(self.specs, list) else []

    def get_features_list(self):
        return self.features if isinstance(self.features, list) else []

    @property
    def main_image(self):
        img = self.images.filter(is_main=True).first()
        if img:
            return img.image
        img = self.images.first()
        if img:
            return img.image
        return self.image  # fallback dla starych wpisów

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('product_detail', kwargs={'slug': self.slug})


class Page(models.Model):
    title = models.CharField(max_length=200, verbose_name='Tytuł')
    slug = models.SlugField(unique=True, verbose_name='Slug (URL)',
                            help_text='Np. "polityka-prywatnosci" → /strony/polityka-prywatnosci/')
    content = models.TextField(verbose_name='Treść (HTML)',
                               help_text='Możesz używać HTML: <h2>, <p>, <ul>, <li>, <strong>, <a href="...">, itd.')
    meta_description = models.CharField(max_length=300, blank=True, verbose_name='Meta description (SEO)')
    show_in_footer = models.BooleanField(default=True, verbose_name='Pokaż w stopce')
    footer_order = models.PositiveSmallIntegerField(default=0, verbose_name='Kolejność w stopce')
    is_active = models.BooleanField(default=True, verbose_name='Aktywna')

    class Meta:
        ordering = ['footer_order', 'title']
        verbose_name = 'Strona informacyjna'
        verbose_name_plural = 'Strony informacyjne'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('page_detail', kwargs={'slug': self.slug})


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='images', verbose_name='Produkt'
    )
    image = models.ImageField(upload_to='products/', verbose_name='Zdjęcie')
    is_main = models.BooleanField(default=False, verbose_name='Zdjęcie główne')
    order = models.PositiveSmallIntegerField(default=0, verbose_name='Kolejność')

    class Meta:
        ordering = ['-is_main', 'order']
        verbose_name = 'Zdjęcie produktu'
        verbose_name_plural = 'Zdjęcia produktu'

    def __str__(self):
        return f"{self.product.name} – {'główne' if self.is_main else f'#{self.order}'}"

    def save(self, *args, **kwargs):
        if self.is_main:
            ProductImage.objects.filter(product=self.product).exclude(pk=self.pk).update(is_main=False)
        _compress = False
        if self.image and self.image.name:
            old = ProductImage.objects.filter(pk=self.pk).values_list('image', flat=True).first() if self.pk else None
            _compress = old != self.image.name
        super().save(*args, **kwargs)
        if _compress:
            compress_image(self.image)
