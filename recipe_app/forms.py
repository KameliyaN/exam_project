from django import forms
from django.core.exceptions import ValidationError

from recipe_app.models import Recipe


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""

    class Meta:
        model = Recipe
        fields = '__all__'
        labels = {
            'time': 'Time(Minutes)'
        }

    def clean_ingredients(self):
        ingredients = self.cleaned_data['ingredients']
        if ', ' not in ingredients:
            raise ValidationError('Please separate the ingredients with comma and space')
        return ingredients
