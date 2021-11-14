from rest_framework import filters
from django.contrib.auth import get_user_model
from apps.biscuit.models import Biscuit
from apps.client.models import Client


def convert_query_params_to_dict(query_params):
    return {
        'created_date': query_params.get('date_one', None),
        'status': query_params.get('status', None),
        'created_date_two': query_params.get('date_two', None),
        'biscuit': query_params.get('biscuit', None),
        'client': query_params.get('client', None)
    }


def convert_biscuit_query_params_to_dict(query_params):
    return {
        'created_date': query_params.get('date_one', None),
        'created_date_two': query_params.get('date_two', None),
        'status': query_params.get('status', None),
        'biscuit': query_params.get('biscuit', None),
        'staff': query_params.get('staff', None)
    }


class SaleBiscuitFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        data = convert_query_params_to_dict(request.query_params)
        data = {k: v for k, v in data.items() if v is not None}
        if 'client' in data:
            client_company = data['client']
            client = Client.objects.filter(company=client_company)
            if client.exists():
                data['client'] = str(client.first().id)
            else:
                data['client'] = str(-1)
        if 'biscuit' in data:
            biscuit_name = Biscuit.objects.filter(name=data['biscuit'])
            if biscuit_name.exists():
                data['biscuit'] = str(biscuit_name.first().id)
            else:
                data['biscuit'] = str(-1)
        if 'created_date' in data and 'created_date_two' in data:
            queryset = queryset.filter(created_date__range=[data['created_date'], data['created_date_two']])
            data.pop('created_date')
            data.pop('created_date_two')
            queryset.filter(**data)
            return queryset
        return queryset.filter(**data)


class AddBiscuitFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        data = convert_query_params_to_dict(request.query_params)
        data = {k: v for k, v in data.items() if v is not None}
        if 'staff' in data:
            first_name = data['staff']
            staff = get_user_model().objects.filter(first_name=first_name)
            if staff.exists():
                data['staff'] = str(staff.first().id)
            else:
                data['staff'] = str(-1)
        if 'biscuit' in data:
            biscuit_name = Biscuit.objects.filter(name=data['biscuit'])
            if biscuit_name.exists():
                data['biscuit'] = str(biscuit_name.first().id)
            else:
                data['biscuit'] = str(-1)
        if 'created_date' in data and 'created_date_two' in data:
            queryset = queryset.filter(created_date__range=[data['created_date'], data['created_date_two']])
            data.pop('created_date')
            data.pop('created_date_two')
            queryset.filter(**data)
            return queryset
        return queryset.filter(**data)
