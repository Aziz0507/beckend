from rest_framework.routers import SimpleRouter

from api.supplier.views.supplier import SupplierModelViewSet

urlpatterns = []

router = SimpleRouter()
router.register(r'', SupplierModelViewSet, basename='supplier')

urlpatterns += router.urls
