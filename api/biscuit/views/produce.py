from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from apps.biscuit.models import ProduceBiscuit
from api.biscuit.utils.filter import AddBiscuitFilter
from api.biscuit.serializers.produce import ProduceBiscuitSerializer, ProduceBiscuitCreateSerializer


class ProduceBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = ProduceBiscuit.objects.all()
    serializer_class = ProduceBiscuitSerializer

    def get_serializer_class(self):
        return ProduceBiscuitCreateSerializer if self.action in ['create', 'update'] else self.serializer_class


class FilterProduceBiscuit(ListAPIView):
    queryset = ProduceBiscuit.objects.all()
    serializer_class = ProduceBiscuitSerializer
    filter_backends = [AddBiscuitFilter]
