from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from planner.forms import PlanForm, RecipeForm, RecipeItemForm, PlanItemForm
from django.shortcuts import redirect, render
from .models import Product, Recipe, Plan, PlanItem
from django.contrib.auth.decorators import login_required
from django.utils import translation
from django.utils.translation import gettext
from django.template.defaulttags import register


@register.filter
def div(value, div):
    return round((value / div) * 100, 2)
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def home(request):
    if request.user.is_authenticated:
        return redirect('planner')
    context = {}
    return render(request, 'planner/home.html', context)


@login_required
def planner(request):
    plans = Plan.objects.filter(user=request.user)
    try:
        language = request.session[translation.LANGUAGE_SESSION_KEY]
    except KeyError:
        language = 'ru'
        request.session[translation.LANGUAGE_SESSION_KEY] = language
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            plan = form.save()
            plan.user = request.user
            plan.save()
            messages.success(request, gettext('Your new plan has been created!'))
            return redirect('planner')
    else:
        form = PlanForm()
    context = {'plans': plans, 'form': form, 'language': language}
    return render(request, 'planner/planner.html', context)


@login_required
def edit_plan(request, pk):
    try:
        plan = Plan.objects.get(pk=pk)
        items = plan.planitem_set.all()
    except ObjectDoesNotExist:
        messages.warning(request, gettext('404: Does not exist.'))
        if request.user.is_authenticated:
            return redirect('planner')
        else:
            return redirect('home')
    if plan.user == request.user:
        try:
            language = request.session[translation.LANGUAGE_SESSION_KEY]
        except KeyError:
            language = 'ru'
            request.session[translation.LANGUAGE_SESSION_KEY] = language
        if plan.type == '3d':
            days = {'1': '1', '2': '2', '3': '3'}
        else:
            days = {'1': '1', '2': '2', '3': '3',
                    '4': '4', '5': '5', '6': '6', '7': '7'}
        day_calories = {}
        day_price = {}
        for k, v in days.items():
            day = v
            planitems = plan.planitem_set.filter(day=day)
            total_calories = sum(
                [item.recipe.get_total_calories for item in planitems])
            total_price = sum([item.recipe.get_total_price for item in planitems])
            day_calories[f'{v}'] = total_calories
            day_price[f'{v}'] = total_price
        if request.method == 'POST':
            form = PlanItemForm(request.POST)
            if form.is_valid():
                _, day = request.POST['select'].split()
                planitem = PlanItem.objects.create(recipe=form.cleaned_data.get('recipe'),
                                                time=form.cleaned_data.get('time'), day=day,
                                                plan=plan)
                
                return redirect('edit-plan', pk)
        else:
            form = PlanItemForm()
        context = {'plan': plan, 'items': items, 'form': form, 'days': days,
                'day_calories': day_calories, 'day_price': day_price, 'language': language}
        return render(request, 'planner/edit_plan.html', context)
    else:
        messages.warning(request, gettext('403: Forbidden.'))
        if request.user.is_authenticated:
            return redirect('planner')
        else:
            return redirect('home')


def products(request):
    products = Product.objects.all()
    try:
        language = request.session[translation.LANGUAGE_SESSION_KEY]
    except KeyError:
        language = 'ru'
        request.session[translation.LANGUAGE_SESSION_KEY] = language

    context = {'products': products, 'language': language}
    return render(request, 'planner/products.html', context)


def recipes(request):
    recipes = Recipe.objects.all()
    try:
        language = request.session[translation.LANGUAGE_SESSION_KEY]
    except KeyError:
        language = 'ru'
        request.session[translation.LANGUAGE_SESSION_KEY] = language
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save()
            recipe.user = request.user
            recipe.save()
            messages.success(request, gettext('Your new recipe has been created'))
            return redirect('recipes')
    else:
        form = RecipeForm()
    context = {'recipes': recipes, 'form': form, 'language': language}
    return render(request, 'planner/recipes.html', context)


def recipe_detail(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    items = recipe.items.all()
    try:
        language = request.session[translation.LANGUAGE_SESSION_KEY]
    except KeyError:
        language = 'ru'
        request.session[translation.LANGUAGE_SESSION_KEY] = language
    context = {'recipe': recipe, 'items': items, 'language': language}
    return render(request, 'planner/recipe_detail.html', context)

@login_required
def delete_recipe(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except ObjectDoesNotExist:
        messages.warning(
                request, gettext(f'404: Object does not exist.'))
        return redirect('recipes')
    if recipe.user == request.user:
        recipe.delete()
        messages.success(request, gettext('You have deleted the recipe!'))
        return redirect('recipes')
    else:
        messages.warning(request, gettext('403: Forbidden.'))
@login_required
def edit_items(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        items = recipe.items.all()
    except ObjectDoesNotExist:
        messages.warning(
                request, gettext(f'404: Object does not exist.'))
        return redirect('recipes')
    if recipe.user == request.user:
        if request.method == 'POST':
            form = RecipeItemForm(request.POST)
            if form.is_valid():
                recipeitem = form.save()
                recipe.items.add(recipeitem)
                
                return redirect('edit-items', pk)
        else:
            form = RecipeItemForm()
        context = {'recipe': recipe, 'items': items, 'form': form}
        return render(request, 'planner/edit_items.html', context)
    else:
        messages.warning(
                request, gettext(f'403: Forbidden.'))
        return redirect('recipes')


@login_required
def delete_item(request, pk, item_pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
        item = recipe.items.get(pk=item_pk)
    except ObjectDoesNotExist:
        messages.warning(request, gettext('404: Does not exist.'))
        return redirect('home')
    if request.user == recipe.user:
        item.delete()
        messages.success(request, gettext('Deleted successfully!'))
        return redirect('edit-items', pk)
    else:
        messages.warning(request, gettext('403: Forbidden.'))
        return redirect('home')
    
@login_required
def delete_plan(request, pk):
    try:
        plan = Plan.objects.get(pk=pk)
    except Plan.DoesNotExist:
        messages.warning(request, gettext('404: Plan does not exist.'))
        return redirect('home')
    if request.user == plan.user:
        plan.delete()
        messages.success(request, gettext('Deleted successfully!'))
        return redirect('planner')
    else:
        messages.warning(request, gettext('403: Forbidden.'))
        return redirect('home')


@login_required
def delete_plan_item(request, pk, item_pk):
    try:
        plan = Plan.objects.get(pk=pk)
        item = plan.planitem_set.get(pk=item_pk)
    except ObjectDoesNotExist:
        messages.warning(request, gettext('404: Does not exist.'))
        return redirect('home')
    if request.user == plan.user:
        item.delete()
        messages.success(request, gettext('Deleted successfully!'))
        return redirect('edit-plan', pk)
    else:
        messages.warning(request, gettext('403: You can not delete that.'))
        return redirect('home')
