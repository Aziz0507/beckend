from django.contrib.auth import get_user_model
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=14)
    xr = models.CharField(max_length=100)
    mfo = models.CharField(max_length=100)
    inn = models.CharField(max_length=100)
    responsible_person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Supplier: {self.name}'

    @property
    def responsible_person_name(self):
        return self.responsible_person.__str__()
