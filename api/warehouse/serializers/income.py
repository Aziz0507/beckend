from rest_framework import serializers

from apps.warehouse.models.income import TakeMoney, Income, ReserveMoney
from api.warehouse.utils.income import subtract_money, subtract_money_update


class TakeMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = TakeMoney
        fields = "__all__"

    def create(self, validated_data):
        subtract_money(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        subtract_money_update(instance, validated_data)
        return super().update(instance, validated_data)


class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class ReserveMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReserveMoney
        fields = "__all__"
