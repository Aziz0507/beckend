from rest_framework import serializers

from apps.warehouse.models.product import WareHouseProduct, WareHouseManufacturedProduct
from api.product.serializers.product import ProductModelSerializer, ManufacturedProductModelSerializer


class WareHouseProductCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseProduct
        fields = '__all__'


class WareHouseProductDetailModelSerializer(serializers.ModelSerializer):
    product = ProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = WareHouseProduct
        fields = (
            'product',
            'quantity',
            'total_price',
            'average_price',
            'unit_of_measurement',
            'currency',
            'created_date'
        )


class WareHouseManufacturedProductCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseManufacturedProduct
        fields = ['manufactured_product']


class WareHouseManufacturedProductDetailModelSerializer(serializers.ModelSerializer):
    manufactured_product = ManufacturedProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = WareHouseManufacturedProduct
        fields = (
            'manufactured_product',
            'quantity',
            'total_price',
            'average_price',
            'unit_of_measurement',
            'created_date'
        )
