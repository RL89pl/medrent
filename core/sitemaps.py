from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Product


class ProductSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Product.objects.filter(is_active=True)

    def lastmod(self, obj):
        return None

    def location(self, obj):
        return obj.get_absolute_url()


class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return ['home', 'oferta']

    def location(self, item):
        return reverse(item)
