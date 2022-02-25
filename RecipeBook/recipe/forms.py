from django import forms
from .models import Recipe, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('author', 'food_name', 'ingredient', 'recipe',)
