from django.db.models import F
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Recipe, RecipeProduct, Product
from django.template import loader
from django.http import HttpResponse


#Это функция добавление продукта в рецепт
#первый параметр это стандартный request
#второй это указанный рецепт
#третий это указанный продукт
#четвертый это указанный вес в граммах
#тут есть функционал который прибавляет единицу в time_used
def add_product_to_recipe(request, recipe_id, product_id, weight):
    if request.method == 'GET':
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        product = get_object_or_404(Product, pk=product_id)

        recipe_product, created = RecipeProduct.objects.get_or_create(recipe=recipe, product=product)
        product.times_used = F('times_used') + 1
        product.save()
        product.refresh_from_db()
        recipe_product.weight_in_grams = weight
        recipe_product.save()

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error'})


#Функция списка рецепта без указанного продукта
def show_recipes_without_product(request, product_id):
    if request.method == 'GET':
        recipes_without_product = Recipe.objects.exclude(recipeproduct__product_id=product_id)

        context = {'recipes': recipes_without_product}
        template = loader.get_template('core/recipes_without_product.html')
        return HttpResponse(template.render(context, request))
