from django.db.models.signals import post_save
from django.dispatch import receiver
from api.warehouse.serializers.biscuit import WareHouseBiscuitCreateModelSerializer
from apps.biscuit.models import Biscuit, PriceList


@receiver(post_save, sender=Biscuit)
def create_biscuit(sender, instance, created=False, **kwargs):
    if created:
        PriceList.objects.create(biscuit=instance, price=instance.price)
        warehouse_biscuit = WareHouseBiscuitCreateModelSerializer(data={'biscuit': instance.id})
        warehouse_biscuit.is_valid(raise_exception=True)
        warehouse_biscuit.save()
