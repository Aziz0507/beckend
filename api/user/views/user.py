from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from api.user.serializers.user import UserModelSerializer, MyTokenObtainPairSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserModelViewSet(ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserModelSerializer

    @action(methods=['get'], detail=False)
    def positions(self, request):
        positions = get_user_model().objects.values('role').distinct()
        return Response(positions)

    @action(methods=['post'], detail=False)
    def employees(self, request):
        employees = get_user_model().objects.filter(role=request.data.get('role')) \
            .values('id', 'first_name', 'last_name', 'middle_name', 'phone_number', 'role', 'salary')
        return Response(employees)

    @action(methods=['post'], detail=False)
    def salary(self, request):
        pk = request.data.get('id')
        salary = request.data.get('salary')
        if pk is None or salary is None:
            return Response({'error': "`pk` or `salary` is not entered"}, status=400)
        try:
            get_user_model().objects.filter(id=pk).update(salary=salary)
        except Exception as e:
            return Response({'error': e}, status=400)
        return Response({'success': True, 'message': "Oylik o'rnatildi"})
