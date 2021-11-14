# Generated by Django 3.2.6 on 2021-09-07 09:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apps_client', '0001_initial'),
        ('apps_biscuit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producebiscuitlog',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='producebiscuit',
            name='biscuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit'),
        ),
        migrations.AddField(
            model_name='pricelist',
            name='biscuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit'),
        ),
        migrations.AddField(
            model_name='incomebiscuit',
            name='biscuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit'),
        ),
        migrations.AddField(
            model_name='buyingbiscuitlog',
            name='biscuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit'),
        ),
        migrations.AddField(
            model_name='buyingbiscuitlog',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_client.client'),
        ),
        migrations.AddField(
            model_name='buyingbiscuit',
            name='biscuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit'),
        ),
        migrations.AddField(
            model_name='buyingbiscuit',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_client.client'),
        ),
        migrations.AddField(
            model_name='addunfitbiscuitlog',
            name='biscuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit'),
        ),
    ]