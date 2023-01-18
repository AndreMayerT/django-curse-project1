from django.shortcuts import render

from recipes.models import Recipe
from utils.recipes.factory import make_recipe

# Create your views here.


def home(req):
    recipes = Recipe.objects.all().order_by('-id')
    return render(req, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
