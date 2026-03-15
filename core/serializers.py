from rest_framework import serializers
from .models import Category, Product, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon_key', 'order']
        read_only_fields = ['id']


class ProductImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image_url', 'is_main', 'order']

    def get_image_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.image.url) if request else obj.image.url


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_url = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug',
            'category', 'category_name', 'subcategory',
            'short_description', 'long_description',
            'image_url', 'images',
            'max_load', 'warranty_years', 'ce_certified',
            'for_rent', 'for_sale',
            'specs', 'features', 'badge',
            'order', 'is_active',
        ]
        read_only_fields = ['id', 'slug', 'image_url', 'images']

    def get_image_url(self, obj):
        img = obj.main_image
        if img:
            request = self.context.get('request')
            return request.build_absolute_uri(img.url) if request else img.url
        return None
