from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.staff.models import SalaryQuantity, StaffSalary, StaffBiscuit, TechnologicalSalary
from api.staff.serializers.salary import (
    SalaryPercentageModelSerializer,
    StaffBiscuitSerializer,
    TechnologicalSalarySerializer,
    StaffSalaryDetailModelSerializer
)


class SalaryPercentageModelViewSet(viewsets.ModelViewSet):
    queryset = SalaryQuantity.objects.all()
    serializer_class = SalaryPercentageModelSerializer


class StaffBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = StaffBiscuit.objects.all()
    serializer_class = StaffBiscuitSerializer


class StaffSalaryListAPIView(ListAPIView):
    queryset = StaffSalary.objects.all()
    serializer_class = StaffSalaryDetailModelSerializer

    def get_queryset(self):
        return self.queryset.filter(staff=self.request.user)


class StaffSalaryDetailAPIView(RetrieveAPIView):
    queryset = StaffSalary.objects.all()
    serializer_class = StaffSalaryDetailModelSerializer


class TechnologicalSalaryAPIView(ListAPIView):
    queryset = TechnologicalSalary.objects.all().order_by('-id')
    serializer_class = TechnologicalSalarySerializer
