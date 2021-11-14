from decimal import Decimal
from django.contrib.auth import get_user_model

from apps.staff.models import TechnologicalSalary


def technological_salary(quantity):
    staff = get_user_model().objects.filter(role='texnolog').order_by('-id').first()
    staff_salary = TechnologicalSalary.objects.filter(staff=staff, status='not_given')
    if staff_salary.exists():
        staff_salary = staff_salary.first()
        staff_salary.add_quantity(Decimal(quantity))
        staff_salary.set_total_price()
        staff_salary.save()
    else:
        staff_salary = TechnologicalSalary.objects.create(staff=staff, status='not_given')
        staff_salary.add_quantity(Decimal(quantity))
        staff_salary.set_total_price()
        staff_salary.save()


def technological_salary_update(instance, new_quantity):
    staff_salary = TechnologicalSalary.objects.filter(status='not_given').first()
    staff_salary.subtract_quantity(instance.quantity)
    staff_salary.set_total_price()
    staff_salary.save()
    staff_salary.add_quantity(new_quantity)
    staff_salary.set_total_price()
    staff_salary.save()
