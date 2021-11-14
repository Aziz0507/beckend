from decimal import Decimal
from collections import defaultdict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.serializers import ValidationError

from api.biscuit.serializers.biscuit import BiscuitCostSerializer
from api.biscuit.utils.price import calculate_biscuit_price, change_status

from apps.biscuit.models import PriceList, ProduceBiscuit
from apps.biscuit.utils.biscuit import get_biscuit


def find_the_same_biscuit(data):
    my_dict = defaultdict(int)
    for i in data:
        my_dict[i['biscuit']] += i['biscuit_cost']
    my_list = [{'biscuit': biscuit, 'biscuit_cost': biscuit_cost} for biscuit, biscuit_cost in my_dict.items()]
    return my_list


class CalculateBiscuitPrice(APIView):
    @staticmethod
    def get(request):
        biscuit_data = calculate_biscuit_price()['data']
        if len(biscuit_data) != 0:
            biscuit_data = find_the_same_biscuit(biscuit_data)
            for i in biscuit_data:
                biscuit = get_biscuit(i['biscuit'])
                number = ProduceBiscuit.objects.filter(for_price='un_calculate', biscuit=biscuit)
                price = Decimal(i['biscuit_cost']) / Decimal(len(number))
                PriceList.objects.create(biscuit=biscuit, price=price)
            change_status()
            return Response({'status': 200})
        else:
            raise ValidationError('pechene ishlab chiqarilmagan!')


class BiscuitCostAPIView(APIView):
    @staticmethod
    def get(request):
        queryset = PriceList.objects.all().order_by('-id')
        serializer = BiscuitCostSerializer(queryset, many=True)
        return Response(serializer.data)
