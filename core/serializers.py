from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'icon_key', 'order']
        read_only_fields = ['id']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'slug',
            'category', 'category_name', 'subcategory',
            'short_description', 'long_description',
            'image', 'image_url',
            'max_load', 'warranty_years', 'ce_certified',
            'for_rent', 'for_sale',
            'specs', 'features', 'badge',
            'order', 'is_active',
        ]
        read_only_fields = ['id', 'slug', 'image_url']
        extra_kwargs = {
            'image': {'write_only': True, 'required': False},
        }

    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None
