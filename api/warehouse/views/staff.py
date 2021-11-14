from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.serializers import ValidationError

from apps.staff.models import StaffSalary
from api.staff.serializers.salary import StaffSalaryModelSerializer, StaffSalaryDetailModelSerializer


class WareHouseStaffSalaryListAPIView(APIView):

    def get_account(self, staff_id):
        try:
            return get_user_model().objects.get(id=staff_id)
        except get_user_model().DoesNotExist:
            raise ValidationError('staff not found')

    def get(self, request):
        staff_id = request.query_params.get('staff_id')
        account = self.get_account(staff_id)
        queryset = StaffSalary.objects.filter(staff=account)
        serializer = StaffSalaryDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class WareHouseStaffSalaryDetailAPIView(RetrieveUpdateAPIView):
    queryset = StaffSalary.objects.all()
    serializer_class = StaffSalaryModelSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = StaffSalaryDetailModelSerializer(instance)
        return Response(serializer.data)
