from django.urls import path
from api.recipe.views.biscuit_recipe import RecipeListAPIView, RecipeDetailAPIView
from api.recipe.views.manufactured_product import (
    ManufacturedProductRecipeListAPIView,
    ManufacturedProductRecipeDetailAPIView
)

urlpatterns = [
    path('', RecipeListAPIView.as_view(), name='biscuit recipe create'),
    path('manufactured_product/', ManufacturedProductRecipeListAPIView.as_view(), name='create_recipe'),
    path('update_or_detail/', RecipeDetailAPIView.as_view(), name='biscuit recipe update and get detail'),
    path('manufactured_product/update_or_detail/', ManufacturedProductRecipeDetailAPIView.as_view(), name='update')

]
