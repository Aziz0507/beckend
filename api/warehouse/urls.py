from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.warehouse.views.box import WareHouseBoxListCreateAPIView
from api.warehouse.views.product import WareHouseProductsListAPIView, WareHouseManufacturedProductListAPIView, \
    WareHouseProductsCreateAPIView
from api.warehouse.views.biscuit import WareHouseBiscuitListAPIView
from api.warehouse.views.staff import WareHouseStaffSalaryListAPIView, WareHouseStaffSalaryDetailAPIView
from api.warehouse.views.unfit_biscuit import WareHouseUnfitBiscuitListAPIView
from api.warehouse.views.income import TakeMoneyModelViewSet, IncomeRetrieveAPIView, ReserveMoneyDetailAPIView

router = SimpleRouter()
router.register('money', TakeMoneyModelViewSet)

urlpatterns = [
    path('take/', include(router.urls)),
    path('products/', WareHouseProductsListAPIView.as_view(), name='warehouse products'),
    path('products/create/', WareHouseProductsCreateAPIView.as_view(), name='warehouse_products_create'),
    path('biscuits/', WareHouseBiscuitListAPIView.as_view(), name='warehouse biscuits'),
    path('unfit/biscuit/', WareHouseUnfitBiscuitListAPIView.as_view(), name='all unfit biscuit'),
    path('income/<int:pk>/', IncomeRetrieveAPIView.as_view(), name='total income'),
    path('staff/salary/lists/', WareHouseStaffSalaryListAPIView.as_view(), name='staff list'),
    path('manufacture/products/', WareHouseManufacturedProductListAPIView.as_view(), name='ware_manufactured_pro'),
    path('reserve_money/<int:pk>/', ReserveMoneyDetailAPIView.as_view()),
    path('staff/salary/detail/<int:pk>/', WareHouseStaffSalaryDetailAPIView.as_view(), name='edit staff salary'),

    path('box/', WareHouseBoxListCreateAPIView.as_view()),
]
