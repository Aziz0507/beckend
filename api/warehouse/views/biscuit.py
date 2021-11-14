from rest_framework.generics import ListAPIView

from apps.warehouse.models.biscuit import WareHouseBiscuit
from api.warehouse.serializers.biscuit import WareHouseBiscuitDetailModelSerializer


class WareHouseBiscuitListAPIView(ListAPIView):
    queryset = WareHouseBiscuit.objects.all()
    serializer_class = WareHouseBiscuitDetailModelSerializer
