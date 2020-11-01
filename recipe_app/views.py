from django.shortcuts import render, redirect

# Create your views here.
from recipe_app.forms import RecipeForm
from recipe_app.models import Recipe


def home_page(request):
    recipies = Recipe.objects.all()
    return render(request, 'recipe_app/index.html', {'recipies': recipies})


def create_recipe(request):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        form = RecipeForm(request.POST)
        return render(request, 'recipe_app/create.html', {'form': form})

    return render(request, 'recipe_app/create.html', {'form': form})


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        return render(request, 'recipe_app/create.html', {'form': form})

    return render(request, 'recipe_app/edit.html', {'form': form, 'recipe': recipe})


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        recipe.delete()
        return redirect('home_page')
    return render(request, 'recipe_app/delete.html', {'recipe': recipe})


def detail_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ingredients = recipe.ingredients.split(', ')

    context = {
        'recipe': recipe,
        'ingredients': ingredients
    }
    return render(request, 'recipe_app/details.html', context)
