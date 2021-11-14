from rest_framework import viewsets

from apps.expense.models.expense import Expense, QuantityExpense
from api.expense.serializers.expense import (
    ExpenseModelSerializer,
    QuantityExpenseModelSerializer,
    QuantityExpenseDetailModelSerializer
)


class ExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseModelSerializer


class QuantityExpenseModelViewSet(viewsets.ModelViewSet):
    queryset = QuantityExpense.objects.all()
    serializer_class = QuantityExpenseModelSerializer

    def get_serializer_class(self):
        return QuantityExpenseDetailModelSerializer if self.action in ['list', 'retrieve'] else self.serializer_class
