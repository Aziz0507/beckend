from rest_framework.serializers import ModelSerializer
from apps.supplier.models.supplier import Supplier


class SupplierSerializer(ModelSerializer):
    class Meta:
        model = Supplier
        fields = (
            'id',
            'name',
            'address',
            'phone_number',
            'xr',
            'mfo',
            'inn',
            'responsible_person',
            'created_at',
            'updated_at',

            # properties
            'responsible_person_name'
        )
