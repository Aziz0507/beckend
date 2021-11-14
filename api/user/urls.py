from django.urls import path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from api.user.views.user import UserModelViewSet, MyTokenObtainPairView

app_name = 'user'

router = routers.DefaultRouter()
router.register('users', UserModelViewSet, basename='users')

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += router.urls
