from rest_framework import serializers

from apps.warehouse.models.biscuit import WareHouseBiscuit
from api.biscuit.serializers.biscuit import BiscuitModelSerializer


class WareHouseBiscuitCreateModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WareHouseBiscuit
        fields = ['biscuit']

    def create(self, validated_data):
        biscuit, _ = WareHouseBiscuit.objects.get_or_create(**validated_data)
        return biscuit


class WareHouseBiscuitDetailModelSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = WareHouseBiscuit
        fields = (
            'biscuit',
            'quantity',
            'total_price',
            'average_price',
            'unit_of_measurement',
            'currency',
            'created_date'
        )
