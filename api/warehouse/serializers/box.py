from django.db.models import Sum
from rest_framework import serializers

from apps.warehouse.models.biscuit import WareHouseBox


class WareHouseBoxModelSerializer(serializers.ModelSerializer):
    biscuit_name = serializers.ReadOnlyField(source='biscuit.name')
    supplier_name = serializers.ReadOnlyField(source='supplier.name')

    class Meta:
        model = WareHouseBox
        fields = (
            'biscuit_name',
            'type_of_box',
            'quantity',
            'supplier_name',
            'note',
            'biscuit',
            'supplier',
        )

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['total'] = WareHouseBox.objects.filter(biscuit=instance.biscuit).aggregate(sum=Sum('quantity')).get('sum')
        return rep
