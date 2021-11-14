from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.biscuit.models import ProduceBiscuit
from apps.biscuit.utils.biscuit import get_biscuit_recipe, check_warehouse_product_quantity
from apps.staff.utils.salary import check_biscuit_price_for_staff
from api.biscuit.serializers.biscuit import BiscuitModelSerializer
from api.biscuit.utils.biscuit import subtract_product, subtract_product_update
from api.staff.utils.salary import technological_salary, technological_salary_update


class ProduceBiscuitCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProduceBiscuit
        fields = ['biscuit', 'quantity']

    def validate(self, attrs):
        if not attrs.get('biscuit'):
            raise serializers.ValidationError({'error': 'biscuit not found'})
        if not attrs.get('quantity'):
            raise serializers.ValidationError({'error': 'quantity not found'})

        recipes = get_biscuit_recipe(attrs.get('biscuit'))
        quantity = attrs.get('quantity')
        check_price = check_biscuit_price_for_staff('texnolog')
        if not get_user_model().objects.filter(role='texnolog').exists():
            raise serializers.ValidationError({'error': 'texnolog not found'})
        if len(recipes) == 0:
            raise serializers.ValidationError({'error': 'Ushbu pecheneni retsepti kiritilmagan!'})
        if check_warehouse_product_quantity(recipes, quantity) != len(recipes):
            raise serializers.ValidationError('Mahsulot yetarli emas!')
        if not check_price:
            raise serializers.ValidationError('Bosh texnologikni pecheneni uchun ish haqqi kiritilmagan!')
        return attrs

    def create(self, validated_data):
        instance = ProduceBiscuit.objects.create(**validated_data)
        technological_salary(validated_data.get('quantity'))
        subtract_product(validated_data)
        return instance

    def update(self, instance, validated_data):
        technological_salary_update(instance, validated_data.get('quantity'))
        subtract_product_update(instance, validated_data)
        instance = super().update(instance, validated_data)
        return instance


class ProduceBiscuitSerializer(serializers.ModelSerializer):
    biscuit = BiscuitModelSerializer(read_only=True, many=False)

    class Meta:
        model = ProduceBiscuit
        fields = (
            'id',
            'biscuit',
            'quantity',
            'currency',
            'status',
            'created_date',
            'modified_date'
        )
