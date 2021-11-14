# Generated by Django 3.2.6 on 2021-09-07 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps_supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='responsible_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]