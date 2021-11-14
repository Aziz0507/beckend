from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.serializers import ValidationError

from apps.biscuit.utils.biscuit import get_biscuit_price
from apps.biscuit.models.sale import BuyingBiscuit, SaleBiscuitPrice
from api.biscuit.utils.filter import SaleBiscuitFilter
from api.biscuit.utils.price import get_biscuit_sale_price
from api.biscuit.serializers.sale import (
    SaleBiscuitModelSerializer,
    SaleBiscuitDetailModelSerializer,
    SaleBiscuitPriceModelSerializer,
    SaleBiscuitPriceDetailModelSerializer
)


class SaleBiscuitModelViewSet(viewsets.ModelViewSet):
    queryset = BuyingBiscuit.objects.all()
    serializer_class = SaleBiscuitModelSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            biscuit = data['biscuit']
            quantity = data['quantity']
        except KeyError:
            raise ValidationError('biscuit or quantity not found')
        price = get_biscuit_sale_price(biscuit)
        data['total_price'] = quantity * price
        serializer = SaleBiscuitModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data
        try:
            biscuit = data['biscuit']
            quantity = data['quantity']
        except KeyError:
            raise ValidationError('biscuit or quantity not found')
        obj = self.get_object()
        price = get_biscuit_sale_price(biscuit)
        data['total_price'] = quantity * price
        serializer = SaleBiscuitModelSerializer(obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_object()
        serializer = SaleBiscuitDetailModelSerializer(queryset, many=False)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = BuyingBiscuit.objects.all()
        serializer = SaleBiscuitDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class FilterSaleBiscuit(ListAPIView):
    queryset = BuyingBiscuit.objects.all()
    serializer_class = SaleBiscuitDetailModelSerializer
    filter_backends = [SaleBiscuitFilter]


class SaleBiscuitPriceAPIView(APIView):
    def get_object(self, pk):
        try:
            return SaleBiscuitPrice.objects.get(pk=pk)
        except SaleBiscuitPrice.DoesNotExist:
            raise ValidationError(f'pk: {pk} not found')

    @staticmethod
    def post(request):
        data = request.data
        try:
            biscuit = data['biscuit']
        except KeyError:
            raise ValidationError('pecheneni topilmadi!')
        default_price = get_biscuit_price(biscuit)
        data['default_price'] = default_price
        serializer = SaleBiscuitPriceModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @staticmethod
    def get(request):
        queryset = SaleBiscuitPrice.objects.all()
        serializer = SaleBiscuitPriceDetailModelSerializer(queryset, many=True)
        return Response(serializer.data)


class SaleBiscuitPriceDetailAPIView(APIView):

    def get_object(self, pk):
        try:
            return SaleBiscuitPrice.objects.get(pk=pk)
        except SaleBiscuitPrice.DoesNotExist:
            raise ValidationError('not found')

    def put(self, request, pk):
        data = request.data
        try:
            biscuit = data['biscuit']
        except KeyError:
            raise ValidationError('pecheneni topilmadi!')
        default_price = get_biscuit_price(biscuit)
        data['default_price'] = default_price
        queryset = self.get_object(pk)
        serializer = SaleBiscuitPriceModelSerializer(queryset, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = SaleBiscuitPriceDetailModelSerializer(queryset, many=False)
        return Response(serializer.data)
