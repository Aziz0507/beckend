from rest_framework import viewsets

from apps.product.models.add_product import AddProduct, AddManufacturedProduct
from api.product.serializers.add_product import (
    ProductAddListModelSerializer,
    ProductAddDetailModelSerializer,
    ProductUpdateModelSerializer,
    ManufacturedProductAddListModelSerializer,
    ManufacturedProductUpdateModelSerializer,
    ManufacturedProductAddDetailModelSerializer
)


class ProductAddModelViewSet(viewsets.ModelViewSet):
    queryset = AddProduct.objects.all()
    serializer_class = ProductAddListModelSerializer

    a2s = {
        'list': ProductAddDetailModelSerializer,
        'retrieve': ProductAddDetailModelSerializer,
        'update': ProductUpdateModelSerializer,
    }

    def get_serializer_class(self):
        return self.a2s[self.action] if self.action in ['list', 'retrieve', 'update'] else self.serializer_class


# new one

class ManufacturedProductAddModelViewSet(viewsets.ModelViewSet):
    queryset = AddManufacturedProduct.objects.all()
    serializer_class = ManufacturedProductAddListModelSerializer

    a2s = {
        'list': ManufacturedProductAddDetailModelSerializer,
        'retrieve': ManufacturedProductAddDetailModelSerializer,
        'update': ManufacturedProductUpdateModelSerializer,
    }

    def get_serializer_class(self):
        return self.a2s[self.action] if self.action in ['list', 'retrieve', 'update'] else self.serializer_class
