import re
from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class PostCategory(models.Model):
    name        = models.CharField(max_length=100, verbose_name='Nazwa')
    slug        = models.SlugField(unique=True, verbose_name='Slug')
    description = models.CharField(max_length=300, blank=True, verbose_name='Opis')

    class Meta:
        verbose_name        = 'Kategoria bloga'
        verbose_name_plural = 'Kategorie bloga'
        ordering            = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_list') + f'?kategoria={self.slug}'


class Tag(models.Model):
    name = models.CharField(max_length=60, verbose_name='Nazwa')
    slug = models.SlugField(unique=True, verbose_name='Slug')

    class Meta:
        verbose_name        = 'Tag'
        verbose_name_plural = 'Tagi'
        ordering            = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_list') + f'?tag={self.slug}'


class Post(models.Model):
    DRAFT     = 'draft'
    PUBLISHED = 'published'
    STATUS_CHOICES = [(DRAFT, 'Szkic'), (PUBLISHED, 'Opublikowany')]

    # ── PODSTAWOWE ────────────────────────────────────────────────────────────
    title       = models.CharField(max_length=200, verbose_name='Tytuł')
    slug        = models.SlugField(unique=True, blank=True, verbose_name='Slug (URL)',
                                   help_text='Wypełniany automatycznie. Zmiana wpływa na URL artykułu.')
    category    = models.ForeignKey(
        PostCategory, null=True, blank=True,
        on_delete=models.SET_NULL, related_name='posts',
        verbose_name='Kategoria'
    )
    tags        = models.ManyToManyField(Tag, blank=True, verbose_name='Tagi')
    author      = models.CharField(max_length=100, default='Redakcja', verbose_name='Autor')
    status      = models.CharField(max_length=10, choices=STATUS_CHOICES,
                                   default=DRAFT, verbose_name='Status')
    is_featured = models.BooleanField(default=False, verbose_name='Wyróżniony',
                                      help_text='Wyróżnione wpisy pojawiają się na stronie głównej.')

    # ── TREŚĆ ─────────────────────────────────────────────────────────────────
    excerpt = models.CharField(
        max_length=500, blank=True, verbose_name='Zajawka',
        help_text='Krótki opis widoczny na liście artykułów i w wynikach wyszukiwarki. Maks. 500 znaków.'
    )
    content = models.TextField(
        verbose_name='Treść (HTML)',
        help_text='Dostępne tagi: <h2>, <h3>, <p>, <ul>, <ol>, <li>, <strong>, <em>, <a>, <blockquote>, <img>.'
    )

    # ── GRAFIKI ───────────────────────────────────────────────────────────────
    cover_image = models.ImageField(upload_to='blog/', null=True, blank=True,
                                    verbose_name='Zdjęcie główne')
    cover_alt   = models.CharField(max_length=200, blank=True, verbose_name='Alt zdjęcia',
                                   help_text='Opis zdjęcia dla czytników ekranu i SEO.')

    # ── SEO ───────────────────────────────────────────────────────────────────
    meta_title       = models.CharField(
        max_length=70, blank=True, verbose_name='Meta title',
        help_text='Domyślnie: tytuł artykułu. Maks. 70 znaków.'
    )
    meta_description = models.CharField(
        max_length=160, blank=True, verbose_name='Meta description',
        help_text='Domyślnie: zajawka artykułu. Maks. 160 znaków.'
    )
    og_image = models.ImageField(
        upload_to='blog/og/', null=True, blank=True,
        verbose_name='OG Image (social media)',
        help_text='Grafika do udostępniania. Zalecany rozmiar: 1200×630 px. Domyślnie: zdjęcie główne.'
    )

    # ── DATY ──────────────────────────────────────────────────────────────────
    published_at = models.DateTimeField(null=True, blank=True, verbose_name='Data publikacji',
                                        help_text='Ustaw datę w przyszłości, aby zaplanować publikację.')
    created_at   = models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')
    updated_at   = models.DateTimeField(auto_now=True,     verbose_name='Zaktualizowano')

    # ── STATYSTYKI ────────────────────────────────────────────────────────────
    reading_time = models.PositiveSmallIntegerField(
        default=1, verbose_name='Czas czytania (min)',
        help_text='Obliczany automatycznie na podstawie długości treści.'
    )

    class Meta:
        verbose_name        = 'Wpis'
        verbose_name_plural = 'Wpisy'
        ordering            = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Auto-generate slug
        if not self.slug:
            base = slugify(self.title)
            slug = base
            i = 1
            while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{i}'
                i += 1
            self.slug = slug

        # Auto-calculate reading time (~200 words/min)
        text = re.sub(r'<[^>]+>', ' ', self.content)
        self.reading_time = max(1, round(len(text.split()) / 200))

        # Auto-set published_at on first publish
        if self.status == self.PUBLISHED and not self.published_at:
            self.published_at = timezone.now()

        _compress_cover = False
        _compress_og    = False
        if self.cover_image and self.cover_image.name:
            old = Post.objects.filter(pk=self.pk).values_list('cover_image', flat=True).first() if self.pk else None
            _compress_cover = old != self.cover_image.name
        if self.og_image and self.og_image.name:
            old = Post.objects.filter(pk=self.pk).values_list('og_image', flat=True).first() if self.pk else None
            _compress_og = old != self.og_image.name

        super().save(*args, **kwargs)

        from core.utils import compress_image
        if _compress_cover:
            compress_image(self.cover_image)
        if _compress_og:
            compress_image(self.og_image)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('blog_detail', kwargs={'slug': self.slug})

    @property
    def effective_meta_title(self):
        return self.meta_title or self.title

    @property
    def effective_meta_description(self):
        return self.meta_description or self.excerpt
