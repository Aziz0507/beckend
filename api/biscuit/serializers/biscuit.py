from decimal import Decimal
from rest_framework.serializers import ModelSerializer, ReadOnlyField

from apps.biscuit.models.biscuit import Biscuit, PriceList, ReturnBiscuit
from apps.warehouse.models import WareHouseBiscuit


class BiscuitModelSerializer(ModelSerializer):
    class Meta:
        model = Biscuit
        fields = "__all__"

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        obj = PriceList.objects.filter(biscuit__id=instance.id).first()
        obj.price = validated_data.get('price', instance.price)
        obj.save()
        return instance


class BiscuitCostSerializer(ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = PriceList
        fields = [
            'id',
            'biscuit',
            'price',
            'currency',
            'created_date',
            'modified_date'
        ]


class ReturnDetailBiscuitCostSerializer(ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)
    client_first_name = ReadOnlyField(source='client.first_name')
    client_last_name = ReadOnlyField(source='client.last_name')

    class Meta:
        model = ReturnBiscuit
        fields = [
            'id',
            'biscuit',
            'comment',
            'quantity',
            'created_date',
            'modified_date',
            'client',
            'client_first_name',
            'client_last_name',
        ]


class ReturnBiscuitSerializer(ModelSerializer):
    class Meta:
        model = ReturnBiscuit
        fields = "__all__"

    def create(self, validated_data):
        biscuit_id = validated_data.get('biscuit')
        quantity = validated_data.get('quantity')
        ware_house_biscuit = WareHouseBiscuit.objects.filter(biscuit_id=biscuit_id).first()
        ware_house_biscuit.add_quantity(Decimal(quantity))
        ware_house_biscuit.set_total_price()
        ware_house_biscuit.set_average_price()
        ware_house_biscuit.save()
        return super().create(validated_data)
