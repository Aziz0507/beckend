from rest_framework import viewsets

from api.order.serializers.order import ClientOrderModelSerializer, ClientOrderDetailModelSerializer
from apps.order.models.order import ClientOrder


class ClientOrderModelViewSet(viewsets.ModelViewSet):
    queryset = ClientOrder.objects.all()
    serializer_class = ClientOrderModelSerializer

    def get_serializer_class(self):
        return ClientOrderDetailModelSerializer if self.action in ['list', 'retrieve'] else self.serializer_class
