from apps.biscuit.models import Biscuit, BuyingBiscuitLog
from apps.biscuit.utils.biscuit import get_warehouse_biscuit
from apps.warehouse.models import WareHouseBiscuit
from apps.warehouse.models.biscuit import WareHouseBox


def check_warehouse_biscuit_quantity(instance, quantity):
    if instance.quantity > quantity:
        return True
    else:
        return False


def sale_biscuit(instance):
    ware_biscuit = get_warehouse_biscuit(instance.biscuit)
    if check_warehouse_biscuit_quantity(ware_biscuit, instance.quantity):
        try:
            products = WareHouseBox.objects.filter(biscuit=instance.biscuit)
            total_quantity = instance.quantity
            for p in products:
                if total_quantity <= 0:
                    break
                if p.quantity < total_quantity:
                    total_quantity -= p.quantity
                    p.quantity = 0
                    p.save()
                else:
                    p.subtract_quantity(instance.quantity)
                    p.save()
                    break
        except Exception as e:
            print(e)
        ware_biscuit.subtract_quantity(instance.quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.set_average_price()
        ware_biscuit.save()
        return True
    else:
        return False


def sale_biscuit_log(instance):
    BuyingBiscuitLog.objects.create(
        sale_id=instance.id,
        biscuit=instance.biscuit,
        quantity= instance.quantity,
        client=instance.client,
        payment_type= instance.payment_type,
        total_price = instance.total_price
    )


def change_sale_biscuit(instance):
    obj = BuyingBiscuitLog.objects.get(sale_id=instance.id)
    ware_biscuit = get_warehouse_biscuit(instance.biscuit)
    if check_warehouse_biscuit_quantity(ware_biscuit, instance.quantity):
        ware_biscuit.add_quantity(obj.quantity)
        try:
            products = WareHouseBox.objects.filter(biscuit=instance.biscuit)
            total_quantity = instance.quantity
            for p in products:
                if total_quantity <= 0:
                    break
                if p.quantity < total_quantity:
                    total_quantity -= p.quantity
                    p.quantity = 0
                    p.save()
                else:
                    p.subtract_quantity(instance.quantity)
                    p.save()
                    break
        except Exception as e:
            print(e)

        ware_biscuit.subtract_quantity(instance.quantity)
        ware_biscuit.set_total_price()
        ware_biscuit.set_average_price()
        ware_biscuit.save()
        obj.quantity = instance.quantity
        obj.biscuit = instance.biscuit
        obj.save()