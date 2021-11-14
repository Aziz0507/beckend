from rest_framework import serializers

from apps.warehouse.models import WareHouseUnfitBiscuit
from api.biscuit.serializers.biscuit import BiscuitModelSerializer


class WareHouseUnfitBiscuitSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(many=False, read_only=True)

    class Meta:
        model = WareHouseUnfitBiscuit
        fields = (
            "id",
            "biscuit",
            "quantity",
            "total_price",
            "created",
            "updated"
        )
