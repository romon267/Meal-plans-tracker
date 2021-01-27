from django.contrib import messages
from planner.forms import PlanForm, RecipeForm, RecipeItemForm, PlanItemForm
from django.shortcuts import redirect, render
from .models import Product, Recipe, Plan, PlanItem
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context = {}
    return render(request, 'planner/home.html', context)

@login_required
def planner(request):
    plans = Plan.objects.filter(user=request.user)
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save()
            plan.user = request.user
            plan.save()
            return redirect('planner')
    else:
        form = PlanForm()
    context = {'plans': plans, 'form': form}
    return render(request, 'planner/planner.html', context)

@login_required
def edit_plan(request, pk):
    plan = Plan.objects.get(pk=pk)
    items = plan.planitem_set.all()
    if plan.type == '3d':
        days = {'1': '1','2': '2','3': '3'}
    else:
        days = {'1': '1','2': '2','3': '3','4': '4','5': '5','6': '6', '7': '7'}
    if request.method == 'POST':
        form = PlanItemForm(request.POST)
        if form.is_valid():
            _, day = request.POST['select'].split()
            planitem = PlanItem.objects.create(recipe=form.cleaned_data.get('recipe'),
                                                time=form.cleaned_data.get('time'), day=day,
                                                plan=plan)
            messages.success(request, f'You have added {planitem.recipe.name} to the plan!')
            return redirect('edit-plan', pk)
    else:
        form = PlanItemForm()
    context = {'plan': plan, 'items': items, 'form': form, 'days': days}
    return render(request, 'planner/edit_plan.html', context)


def products(request):
    products = Product.objects.all()
    
    context = {'products': products}
    return render(request, 'planner/products.html', context)


def recipes(request):
    recipes = Recipe.objects.all()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.user = request.user
            recipe.save()
            return redirect('recipes')
    else:
        form = RecipeForm()
    context = {'recipes': recipes, 'form':form}
    return render(request, 'planner/recipes.html', context)


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    items = recipe.items.all()
    context = {'recipe': recipe, 'items': items}
    return render(request, 'planner/recipe_detail.html', context)

@login_required
def edit_items(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    items = recipe.items.all()
    if request.method == 'POST':
        form = RecipeItemForm(request.POST)
        if form.is_valid():
            recipeitem = form.save()
            recipe.items.add(recipeitem)
            messages.success(request, f'You have added {recipeitem.product.name} to the recipe!')
            return redirect('edit-items', pk)
    else:
        form = RecipeItemForm()
    context = {'recipe': recipe, 'items': items, 'form': form}
    return render(request, 'planner/edit_items.html', context)

@login_required
def delete_item(request, pk, item_pk):
    recipe = Recipe.objects.get(pk=pk)
    item = recipe.items.get(pk=item_pk)
    item.delete()
    return redirect('edit-items', pk)