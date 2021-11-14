from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView

from apps.warehouse.models.income import TakeMoney, Income, ReserveMoney
from api.warehouse.serializers.income import TakeMoneySerializer, IncomeSerializer, ReserveMoneySerializer


class TakeMoneyModelViewSet(viewsets.ModelViewSet):
    queryset = TakeMoney.objects.all()
    serializer_class = TakeMoneySerializer


class IncomeRetrieveAPIView(RetrieveAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class ReserveMoneyDetailAPIView(RetrieveUpdateAPIView):
    queryset = ReserveMoney.objects.all()
    serializer_class = ReserveMoneySerializer
