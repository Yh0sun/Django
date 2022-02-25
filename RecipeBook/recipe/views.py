from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


from .forms import RecipeForm, CommentForm
from .models import Recipe, Comment


@login_required
def comment_add(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = CommentForm()
    return render(request, 'recipe/comment_add.html', {'form': form})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    recipe_pk = comment.recipe.pk
    comment.delete()
    return redirect('recipe_detail', pk=recipe_pk)


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('recipe_detail', pk=comment.recipe.pk)


def recipe_list(request):
    recipes = Recipe.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    paginator = Paginator(recipes, 3)
    try:
        page_number = request.GET.get('page')
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return render(request, 'recipe/recipe_list.html', {'recipes': page})



def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe/recipe_detail.html', {'recipe': recipe})

@login_required
def recipe_new(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            cleaned_data_dict = form.cleaned_data
            recipe = Recipe.objects.create(
                author=request.user,
                food_name=cleaned_data_dict['food_name'],
                ingredient=cleaned_data_dict['ingredient'],
                recipe=cleaned_data_dict['recipe'],
                created_date=timezone.now()
            )
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipe/recipe_edit.html', {'recipeForm': form})


@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.created_date = timezone.now()
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)

    return render(request, 'recipe/recipe_edit.html', {'recipeForm': form})


@login_required
def recipe_remove(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    recipe.delete()
    return redirect('recipe_list')