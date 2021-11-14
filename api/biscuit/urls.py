from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.biscuit.views.biscuit import BiscuitModelViewSet, ReturnBiscuitModelViewSet
from api.biscuit.views.price import CalculateBiscuitPrice, BiscuitCostAPIView

from api.biscuit.views.produce import ProduceBiscuitModelViewSet, FilterProduceBiscuit
from api.biscuit.views.unfit_biscuit import UnFitBiscuitModelViewSet
from api.biscuit.views.sale import (
    SaleBiscuitModelViewSet,
    FilterSaleBiscuit,
    SaleBiscuitPriceAPIView,
    SaleBiscuitPriceDetailAPIView
)

router = SimpleRouter()
router_unfit = SimpleRouter()
router_api = SimpleRouter()
router_api_sale = SimpleRouter()
router_return = SimpleRouter()

router.register('', BiscuitModelViewSet)
router_unfit.register('unfit', UnFitBiscuitModelViewSet)
router_api.register('produce', ProduceBiscuitModelViewSet)
router_api_sale.register('sale', SaleBiscuitModelViewSet)
router_return.register('return', ReturnBiscuitModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/', include(router_unfit.urls)),
    path('staff/', include(router_api.urls)),
    path('company/', include(router_api_sale.urls)),
    path('saled/filter/', FilterSaleBiscuit.as_view(), name='filter saled biscuits'),
    path('produced/filter/', FilterProduceBiscuit.as_view(), name='filter produced biscuits'),
    path('take/price/', CalculateBiscuitPrice.as_view(), name='take biscuit price'),
    path('sale/price/', SaleBiscuitPriceAPIView.as_view(), name='put sale biscuit price'),
    path('sale/price/<int:pk>/', SaleBiscuitPriceDetailAPIView.as_view(), name='detail sale biscuit price'),
    path('default/cost/', BiscuitCostAPIView.as_view(), name='biscuit cost'),
    path('biscuits/', include(router_return.urls))
]
