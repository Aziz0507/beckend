from rest_framework.generics import ListAPIView, CreateAPIView

from apps.warehouse.models.biscuit import WareHouseBiscuit
from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct
from api.warehouse.serializers.biscuit import WareHouseBiscuitDetailModelSerializer
from api.warehouse.serializers.product import (
    WareHouseProductDetailModelSerializer,
    WareHouseManufacturedProductDetailModelSerializer, WareHouseProductCreateModelSerializer
)


class WareHouseProductsListAPIView(ListAPIView):
    queryset = WareHouseProduct.objects.all()
    serializer_class = WareHouseProductDetailModelSerializer


class WareHouseProductsCreateAPIView(CreateAPIView):
    queryset = WareHouseProduct.objects.all()
    serializer_class = WareHouseProductCreateModelSerializer


class WareHouseBiscuitAPIView(ListAPIView):
    queryset = WareHouseBiscuit.objects.all()
    serializer_class = WareHouseBiscuitDetailModelSerializer


class WareHouseManufacturedProductListAPIView(ListAPIView):
    queryset = WareHouseManufacturedProduct.objects.all()
    serializer_class = WareHouseManufacturedProductDetailModelSerializer
