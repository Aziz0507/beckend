from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

from api import views

schema_view = get_schema_view(title="Surur Server Monitoring API")

urlpatterns = [
    path('admin/', admin.site.urls),

    path('schema', schema_view),
    path('docs/', include_docs_urls(title="Surur", description="Surur Backend API docs"), name='rest_docs'),
    path('swagger/json', views.schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/yaml', views.schema_view.without_ui(cache_timeout=0), name='schema-yaml'),
    path('swagger/', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', views.schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/user/', include('api.user.urls')),
    path('api/v1/product/', include('api.product.urls')),
    path('api/v1/warehouse/', include('api.warehouse.urls')),
    path('api/v1/supplier/', include('api.supplier.urls')),
    path('api/v1/biscuit/', include('api.biscuit.urls')),
    path('api/v1/recipe/', include('api.recipe.urls')),
    path('api/v1/expense/', include('api.expense.urls')),
    path('api/v1/client/', include('api.client.urls')),
    path('api/v1/staff/', include('api.staff.urls')),
    path('api/v1/order/', include('api.order.urls'))
]
