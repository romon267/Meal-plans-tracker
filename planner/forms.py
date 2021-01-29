from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import Plan, PlanItem, Recipe, RecipeItem
from django.contrib.auth.models import User

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']

class RecipeItemForm(ModelForm):
    class Meta:
        model = RecipeItem
        fields = '__all__'

class PlanForm(ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'type']

class PlanItemForm(ModelForm):
    recipe = forms.ModelChoiceField(queryset=Recipe.objects.filter(user=1))
    class Meta:
        model = PlanItem
        fields = ['time', 'recipe']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(PlanItemForm, self).__init__(*args, **kwargs)
        self.fields['recipe'].queryset = Recipe.objects.filter(user = user).union(Recipe.objects.filter(user_added = user))