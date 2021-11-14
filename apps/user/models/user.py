from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator


class CustomUserManager(BaseUserManager):

    def _create_user(self, phone_number, password, **extra_fields):
        now = timezone.now()
        if not phone_number:
            raise ValueError('The given phone_number must be set')
        user = self.model(phone_number=phone_number, is_active=True, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, is_provider=None, **extra_fields):
        return self._create_user(phone_number, password, **extra_fields)

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self._create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    ROLE = (
        ('director', 'director'),  # director
        ('manager', 'manager'),  # sotuv
        ('texnolog', 'texnolog'),  # texnolog
        ('staff', 'staff'),  # ish yurutuvchi
        ('warehouseman', 'warehouseman'),  # omborchi
        ('driver', 'driver'),  # haydovchi
        ('businesmaneger', 'businesmaneger'),
    )
    phone_regex = RegexValidator(regex=r'^998\d{9}$', message="Phone number must be like this `998901234567`")

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=14, unique=True)
    address = models.TextField(null=True, blank=True)
    birthday = models.DateField()

    role = models.CharField(max_length=30, choices=ROLE, blank=True, null=True)

    started_at = models.DateField()
    order_number = models.CharField(max_length=20, null=True, blank=True)
    note = models.CharField(max_length=250, null=True, blank=True)
    salary = models.FloatField(default=0)

    username = None
    email = None

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
