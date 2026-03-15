from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('order')
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.query_params.get('category')
        active = self.request.query_params.get('active')
        if category:
            qs = qs.filter(category__slug=category)
        if active is not None:
            qs = qs.filter(is_active=active.lower() in ('1', 'true', 'yes'))
        return qs

    @action(detail=True, methods=['post'], parser_classes=[MultiPartParser], url_path='image')
    def upload_image(self, request, slug=None):
        product = self.get_object()
        file = request.FILES.get('image')
        if not file:
            return Response({'detail': 'Brak pliku (pole: image).'}, status=status.HTTP_400_BAD_REQUEST)
        product.image = file
        product.save(update_fields=['image'])
        serializer = self.get_serializer(product, context={'request': request})
        return Response({'image_url': serializer.data['image_url']}, status=status.HTTP_200_OK)
