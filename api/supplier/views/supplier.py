from rest_framework.viewsets import ModelViewSet

from apps.supplier.models import Supplier
from api.supplier.serializers.supplier import SupplierSerializer


class SupplierModelViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
