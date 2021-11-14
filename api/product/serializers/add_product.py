from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ValidationError

from apps.biscuit.utils.biscuit import check_warehouse_product_quantity
from apps.product.models.add_product import AddProduct, AddManufacturedProduct
from api.supplier.serializers.supplier import SupplierSerializer
from api.product.utils.product import (
    add_product_to_warehouse,
    add_product_to_warehouse_update,
    manufactured_product_add,
    manufactured_product_add_update
)
from api.product.serializers.product import (
    ManufacturedProductModelSerializer,
    ProductDetailSerializer
)


class ProductAddListModelSerializer(ModelSerializer):
    class Meta:
        model = AddProduct
        fields = (
            'product',
            'quantity',
            'currency',
            'price',
            'supplier'
        )

    def validate(self, attrs):
        if not attrs.get('product'):
            raise ValidationError({'error': 'Product not found'})
        if not attrs.get('quantity'):
            raise ValidationError({'error': 'quantity not found'})
        if not attrs.get('currency'):
            raise ValidationError({'error': 'currency not found'})
        if not attrs.get('price'):
            raise ValidationError({'error': 'price not found'})
        if not attrs.get('supplier'):
            raise ValidationError({'error': 'supplier not found'})
        return attrs

    def create(self, validated_data):
        add_product_to_warehouse(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        add_product_to_warehouse_update(instance, validated_data)
        return super().update(instance, validated_data)


class ProductAddDetailModelSerializer(ModelSerializer):
    product = ProductDetailSerializer(read_only=True, many=False)
    supplier = SupplierSerializer(read_only=True, many=False)

    class Meta:
        model = AddProduct
        fields = (
            'id',
            'product',
            'quantity',
            'currency',
            'price',
            'total_price',
            'supplier',
            'created_date'
        )


class ProductUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = AddProduct
        fields = (
            'product',
            'quantity',
            'price'
        )


class ManufacturedProductAddListModelSerializer(ModelSerializer):
    class Meta:
        model = AddManufacturedProduct
        fields = (
            'product',
            'quantity'
        )

    def validate(self, attrs):
        from apps.product.utils.product import get_product_recipe
        recipes = get_product_recipe(attrs.get('product'))
        if check_warehouse_product_quantity(recipes, attrs.get('quantity')) != len(recipes):
            raise ValidationError({'error': 'not enough products in warehouse'})
        if len(recipes) == 0:
            raise ValidationError({'error': 'Product Recipe not found'})
        return attrs

    def create(self, validated_data):
        manufactured_product_add(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        manufactured_product_add_update(instance, validated_data)
        return super().create(validated_data)


class ManufacturedProductAddDetailModelSerializer(ModelSerializer):
    product = ManufacturedProductModelSerializer(read_only=True, many=False)

    class Meta:
        model = AddManufacturedProduct
        fields = (
            'id',
            'product',
            'quantity',
            'created_date'
        )


class ManufacturedProductUpdateModelSerializer(ModelSerializer):
    class Meta:
        model = AddManufacturedProduct
        fields = (
            'product',
            'quantity',
        )

    def update(self, instance, validated_data):
        from apps.product.utils.product import get_product_recipe
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        recipes = get_product_recipe(product)
        if check_warehouse_product_quantity(recipes, quantity) == len(recipes):
            return super().update(instance, validated_data)
        else:
            raise ValidationError('not enough products in warehouse')
