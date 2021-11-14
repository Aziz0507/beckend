# Generated by Django 3.2.6 on 2021-09-18 08:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apps_user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='order_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='salary',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='customuser',
            name='started_at',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]