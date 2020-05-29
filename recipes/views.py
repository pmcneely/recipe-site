from django.shortcuts import render
from recipes.models import Recipe

import json

# Create your views here.
def recipe_index(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipe_index.html', context)

def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    context = {
        'recipe': recipe.title,
        'steps': json.dumps(recipe.steps),
        'ingredients': json.dumps(recipe.ingredients)
    }
    return render(request, 'recipe_detail.html', context)
