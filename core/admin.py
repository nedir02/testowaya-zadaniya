from django.contrib import admin
from .models import Product, Recipe, RecipeProduct

admin.site.register(Product)
admin.site.register(Recipe)
admin.site.register(RecipeProduct)
