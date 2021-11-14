from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.order.views.order import ClientOrderModelViewSet

router = DefaultRouter()
router.register(r'orders', ClientOrderModelViewSet)

urlpatterns = [
    path('client/', include(router.urls)),
]
