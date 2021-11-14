from rest_framework import serializers

from apps.biscuit.models.sale import BuyingBiscuit, SaleBiscuitPrice
from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.client.serializers.client import ClientModelSerializer
from api.biscuit.utils.biscuit import sale_biscuit_to_client, sale_biscuit_to_client_update


class SaleBiscuitModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuyingBiscuit
        fields = "__all__"

    def validate(self, attrs):
        from apps.biscuit.utils.sale import check_warehouse_biscuit_quantity
        from apps.biscuit.utils.biscuit import get_warehouse_biscuit
        if not attrs.get('biscuit'):
            raise serializers.ValidationError({'error': 'Biscuit not found'})
        if not attrs.get('quantity'):
            raise serializers.ValidationError({'error': 'quantity not found'})
        if not attrs.get('comment'):
            raise serializers.ValidationError({'error': 'comment not found'})
        if not attrs.get('payment_type'):
            raise serializers.ValidationError({'error': 'payment_type not found'})
        if not attrs.get('client'):
            raise serializers.ValidationError({'error': 'client not found'})
        ware_biscuit = get_warehouse_biscuit(attrs.get('biscuit'))
        quantity = attrs.get('quantity')

        if not check_warehouse_biscuit_quantity(ware_biscuit, quantity):
            raise serializers.ValidationError('Mahsulot yetarli emas!')
        return attrs

    def create(self, validated_data):
        instance, _ = BuyingBiscuit.objects.get_or_create(**validated_data)
        sale_biscuit_to_client(validated_data)
        return instance

    def update(self, instance, validated_data):
        sale_biscuit_to_client_update(instance, validated_data)
        return super().update(instance, validated_data)


class SaleBiscuitDetailModelSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)
    client = ClientModelSerializer(read_only=True, many=False)

    class Meta:
        model = BuyingBiscuit
        fields = (
            'id',
            'biscuit',
            'quantity',
            'currency',
            'total_price',
            'comment',
            'payment_type',
            'status',
            'client',
            'created_date',
            'modified_date'
        )


class SaleBiscuitPriceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleBiscuitPrice
        fields = (
            'biscuit',
            'sale_price',
            'default_price'
        )


class SaleBiscuitPriceDetailModelSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = SaleBiscuitPrice
        fields = (
            'biscuit',
            'sale_price',
            'default_price',
            'created_date',
            'modified_date'
        )
