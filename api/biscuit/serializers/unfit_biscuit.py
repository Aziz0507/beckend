from rest_framework import serializers

from apps.biscuit.models import UnfitBiscuit
from apps.warehouse.models import WareHouseUnfitBiscuit
from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.biscuit.utils.biscuit import unfit_biscuit_add_quantity, unfit_biscuit_subtract_quantity


class UnfitBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnfitBiscuit
        fields = (
            'biscuit',
            'quantity',
            'description',
            'status'
        )

    def validate(self, attrs):
        if not attrs.get('biscuit'):
            raise serializers.ValidationError({'error': 'Biscuit not found'})
        if not attrs.get('quantity'):
            raise serializers.ValidationError({'error': 'quantity not found'})
        if not attrs.get('status'):
            raise serializers.ValidationError({'error': 'status not found'})
        if not attrs.get('description'):
            raise serializers.ValidationError({'error': 'description not found'})
        return attrs

    def create(self, validated_data):
        unfit_biscuit, _ = WareHouseUnfitBiscuit.objects.get_or_create(biscuit=validated_data.get('biscuit'),
                                                                       status=validated_data.get('status'))
        unfit_biscuit_add_quantity(validated_data, unfit_biscuit)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        unfit_biscuit_subtract_quantity(instance, validated_data)
        return super().update(instance, validated_data)


class UnfitBiscuitDetailSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = UnfitBiscuit
        fields = (
            'id',
            'biscuit',
            'status',
            'quantity',
            'description',
            'total_price',
        )
