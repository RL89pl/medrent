from django.contrib import admin
from .models import Category, Product, ProductImage, SiteSettings, ContactMessage, Page


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'product', 'created_at']
    list_filter = ['created_at', 'product__category']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'phone', 'product', 'message', 'created_at']
    ordering = ['-created_at']

    def has_add_permission(self, request):
        return False


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Logo i marka', {
            'fields': ('logo', 'favicon'),
        }),
        ('SEO', {
            'fields': ('meta_description', 'og_image'),
        }),
        ('Hero – sekcja główna', {
            'fields': ('hero_image', 'hero_eyebrow', 'hero_title1', 'hero_title2', 'hero_subtitle'),
        }),
        ('Usługi – 3 kafelki', {
            'fields': (
                'service1_title', 'service1_desc',
                'service2_title', 'service2_desc',
                'service3_title', 'service3_desc',
            ),
        }),
        ('O nas', {
            'fields': (
                'about_image', 'about_tag', 'about_title', 'about_lead', 'about_body',
                'about_check_items',
                'about_stat1_number', 'about_stat1_label',
                'about_stat2_number', 'about_stat2_label',
            ),
        }),
        ('Kontakt', {
            'fields': (
                'contact_phone', 'contact_phone_hours',
                'contact_email', 'contact_email_note',
                'contact_address', 'contact_address_note',
            ),
        }),
    )

    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'show_in_footer', 'footer_order', 'is_active']
    list_editable = ['show_in_footer', 'footer_order', 'is_active']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'is_active'),
        }),
        ('Treść', {
            'fields': ('content',),
            'description': (
                'Wpisz treść w HTML. Dostępne tagi: '
                '&lt;h2&gt;, &lt;h3&gt;, &lt;p&gt;, &lt;ul&gt;, &lt;li&gt;, '
                '&lt;strong&gt;, &lt;em&gt;, &lt;a href="..."&gt;, &lt;br&gt;.'
            ),
        }),
        ('SEO', {
            'fields': ('meta_description',),
            'classes': ('collapse',),
        }),
        ('Stopka', {
            'fields': ('show_in_footer', 'footer_order'),
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'order']
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order']


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', 'is_main', 'order']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'subcategory', 'for_rent', 'for_sale', 'is_active', 'order']
    list_filter = ['category', 'for_rent', 'for_sale', 'ce_certified', 'is_active']
    search_fields = ['name', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order', 'is_active']
    inlines = [ProductImageInline]
    fieldsets = (
        (None, {'fields': ('name', 'slug', 'category', 'subcategory', 'is_active', 'order')}),
        ('Opisy', {'fields': ('short_description', 'long_description')}),
        ('Parametry', {'fields': ('max_load', 'warranty_years', 'ce_certified', 'badge')}),
        ('Dostępność', {'fields': ('for_rent', 'for_sale')}),
        ('Dane techniczne i cechy', {'fields': ('specs', 'features')}),
    )
