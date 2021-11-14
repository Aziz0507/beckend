from rest_framework import viewsets

from apps.client.models.client import Client
from api.client.serializers.client import ClientModelSerializer


class ClientModelViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientModelSerializer
