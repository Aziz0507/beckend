# Generated by Django 3.2.6 on 2021-09-15 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps_supplier', '0002_supplier_responsible_person'),
        ('apps_biscuit', '0003_auto_20210910_1752'),
        ('apps_warehouse', '0002_warehousebox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='warehousebox',
            name='product',
        ),
        migrations.AddField(
            model_name='warehousebox',
            name='biscuit',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps_biscuit.biscuit'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='warehousebox',
            name='supplier',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='apps_supplier.supplier'),
            preserve_default=False,
        ),
    ]
