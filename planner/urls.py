from django.urls import path
from . import views as planner_views

urlpatterns = [
    path('', planner_views.home, name='home'),
    path('planner/', planner_views.planner, name='planner'),
    path('planner/edit/<int:pk>/', planner_views.edit_plan, name='edit-plan'),
    path('products/', planner_views.products, name='products'),
    path('recipes/', planner_views.recipes, name='recipes'),
    path('recipes/<int:pk>/', planner_views.recipe_detail, name='recipe-detail'),
    path('recipes/edit/<int:pk>', planner_views.edit_items, name='edit-items'),
    path('recipes/edit/<int:pk>/delete-item/<int:item_pk>', planner_views.delete_item, name='delete-item'),
]
