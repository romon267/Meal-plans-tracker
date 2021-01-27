from django.db.models.base import Model
from django.forms import ModelForm
from .models import Plan, PlanItem, Recipe, RecipeItem

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
    class Meta:
        model = PlanItem
        fields = ['time', 'recipe']