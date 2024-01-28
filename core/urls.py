from django.urls import path
from .views import add_product_to_recipe, show_recipes_without_product

urlpatterns = [
    path('add_product_to_recipe/<int:recipe_id>/<int:product_id>/<int:weight>/', add_product_to_recipe, name='add_product_to_recipe'),
    path('show_recipes_without_product/<int:product_id>/', show_recipes_without_product, name='show_recipes_without_product'),
]
