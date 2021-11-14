from rest_framework.generics import ListCreateAPIView

from api.warehouse.serializers.box import WareHouseBoxModelSerializer
from apps.warehouse.models.biscuit import WareHouseBox


class WareHouseBoxListCreateAPIView(ListCreateAPIView):
    queryset = WareHouseBox.objects.all()
    serializer_class = WareHouseBoxModelSerializer
