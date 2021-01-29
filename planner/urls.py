from django.urls import path
from . import views as planner_views

urlpatterns = [
    path('', planner_views.home, name='home'),
    path('planner/', planner_views.planner, name='planner'),
    path('planner/edit/<int:pk>/', planner_views.edit_plan, name='edit-plan'),
    path('planner/delete/<int:pk>/', planner_views.delete_plan, name='delete-plan'),
    path('planner/delete/<int:pk>/delete-item/<int:item_pk>/', planner_views.delete_plan_item, name='delete-plan-item'),
    path('products/', planner_views.products, name='products'),
    path('recipes/', planner_views.recipes, name='recipes'),
    path('user_recipes/<int:pk>/', planner_views.user_recipes, name='user-recipes'),
    path('recipes/<int:pk>/', planner_views.recipe_detail, name='recipe-detail'),
    path('recipes/save/<int:pk>/', planner_views.save_recipe, name='save-recipe'),
    path('recipes/remove/<int:pk>/', planner_views.remove_recipe, name='remove-recipe'),
    path('recipes/delete/<int:pk>/', planner_views.delete_recipe, name='delete-recipe'),
    path('recipes/edit/<int:pk>/', planner_views.edit_items, name='edit-items'),
    path('recipes/edit/<int:pk>/delete-item/<int:item_pk>/', planner_views.delete_item, name='delete-item'),
]
