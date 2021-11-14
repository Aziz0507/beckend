from rest_framework import viewsets

from apps.product.models.product import Product, ManufacturedProduct
from api.product.serializers.product import (
    ProductModelSerializer,
    ManufacturedProductModelSerializer,
    ProductDetailSerializer
)


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer

    def get_serializer_class(self):
        return ProductDetailSerializer if self.action in ['list', 'retrieve'] else self.serializer_class


class ManufacturedProductModelViewSet(viewsets.ModelViewSet):
    queryset = ManufacturedProduct.objects.all()
    serializer_class = ManufacturedProductModelSerializer
