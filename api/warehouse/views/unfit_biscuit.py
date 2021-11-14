from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

from apps.warehouse.models.unfit_biscuit import WareHouseUnfitBiscuit
from api.warehouse.serializers.unfit_biscuit import WareHouseUnfitBiscuitSerializer


class WareHouseUnfitBiscuitListAPIView(ListAPIView):
    queryset = WareHouseUnfitBiscuit.objects.filter(status='unrecyclable')
    serializer_class = WareHouseUnfitBiscuitSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']
