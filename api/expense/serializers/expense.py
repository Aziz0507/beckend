from rest_framework import serializers

from apps.expense.models.expense import Expense, QuantityExpense


class ExpenseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"


class QuantityExpenseModelSerializer(serializers.ModelSerializer):
    name = serializers.CharField(help_text='Chiqim nomi', required=True, write_only=True)

    class Meta:
        model = QuantityExpense
        fields = (
            'cost',
            'currency',
            'status',
            'payment_method',
            'note',

            # serializer fields
            'name'
        )

    def create(self, validated_data):
        name = validated_data.pop('name')
        expense, _ = Expense.objects.get_or_create(name=name)
        return QuantityExpense.objects.create(expense=expense, **validated_data)


class QuantityExpenseDetailModelSerializer(serializers.ModelSerializer):
    expense = ExpenseModelSerializer(read_only=True, many=False)

    class Meta:
        model = QuantityExpense
        fields = (
            'id',
            'expense',
            'cost',
            'currency',
            'status',
            'created_date',
            'modified_date',
            'payment_method',
            'note',
        )
