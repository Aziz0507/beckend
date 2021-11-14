from rest_framework import viewsets

from api.biscuit.serializers.unfit_biscuit import (
    UnfitBiscuit,
    UnfitBiscuitCreateSerializer,
    UnfitBiscuitDetailSerializer
)


class UnFitBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = UnfitBiscuit.objects.all()
    serializer_class = UnfitBiscuitCreateSerializer

    def get_serializer_class(self):
        return UnfitBiscuitDetailSerializer if self.action in ['list', 'retrieve'] else self.serializer_class
