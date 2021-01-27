from django.contrib import admin
from .models import Product, Plan, PlanItem, Recipe, RecipeItem

admin.site.register(Product)
admin.site.register(Plan)
admin.site.register(PlanItem)
admin.site.register(RecipeItem)
admin.site.register(Recipe)