from django.contrib import admin
from django.utils.html import format_html
from .models import Post, PostCategory, Tag


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display  = ['name', 'slug', 'post_count']
    prepopulated_fields = {'slug': ('name',)}

    def post_count(self, obj):
        return obj.posts.count()
    post_count.short_description = 'Liczba wpisów'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['title', 'category', 'status', 'is_featured', 'published_at', 'reading_time', 'cover_preview']
    list_filter   = ['status', 'is_featured', 'category']
    list_editable = ['status', 'is_featured']
    search_fields = ['title', 'excerpt', 'content', 'author']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    date_hierarchy = 'published_at'
    ordering = ['-published_at', '-created_at']

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'status', 'is_featured'),
        }),
        ('Treść', {
            'fields': ('excerpt', 'content'),
            'description': (
                'Treść można pisać w HTML. Dostępne tagi: '
                '&lt;h2&gt;, &lt;h3&gt;, &lt;p&gt;, &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt;, '
                '&lt;strong&gt;, &lt;em&gt;, &lt;a href="..."&gt;, &lt;blockquote&gt;, '
                '&lt;img src="..."&gt;.'
            ),
        }),
        ('Klasyfikacja', {
            'fields': ('category', 'tags', 'author'),
        }),
        ('Grafika', {
            'fields': ('cover_image', 'cover_alt'),
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'og_image'),
            'classes': ('collapse',),
            'description': (
                'Pola SEO są opcjonalne. Jeśli puste, używane są: tytuł artykułu (meta title) '
                'i zajawka (meta description).'
            ),
        }),
        ('Publikacja', {
            'fields': ('published_at', 'reading_time'),
            'description': (
                'Data publikacji jest ustawiana automatycznie przy pierwszej zmianie statusu na '
                '"Opublikowany". Czas czytania jest obliczany automatycznie.'
            ),
        }),
    )

    readonly_fields = ['reading_time']

    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" style="height:40px;width:60px;object-fit:cover;border-radius:4px;">',
                obj.cover_image.url
            )
        return '—'
    cover_preview.short_description = 'Okładka'
