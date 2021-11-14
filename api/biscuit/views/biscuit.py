from rest_framework import viewsets

from apps.biscuit.models.biscuit import Biscuit, ReturnBiscuit
from api.biscuit.serializers.biscuit import (
    BiscuitModelSerializer,
    ReturnBiscuitSerializer,
    ReturnDetailBiscuitCostSerializer
)


class BiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = Biscuit.objects.all()
    serializer_class = BiscuitModelSerializer


class ReturnBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = ReturnBiscuit.objects.all()
    serializer_class = ReturnBiscuitSerializer

    def get_serializer_class(self):
        return ReturnDetailBiscuitCostSerializer if self.action in ['list', 'retrieve'] else self.serializer_class
