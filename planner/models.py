from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'id:{self.id}, {self.name}, price:{self.price}, cals:{self.calories}'


class RecipeItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, default=None)
    
    grams = models.IntegerField(default=0, null=True, blank=True)

    @property
    def get_total(self):
        total = (self.product.price / 100) * self.grams
        return total

    def __str__(self):
        return f'id:{self.id}'

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=800)
    items = models.ManyToManyField(RecipeItem, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    @property
    def get_total_price(self):
        recipeitems = self.items.all()
        total = sum([item.get_total for item in recipeitems])
        return total

    @property
    def get_total_calories(self):
        recipeitems = self.items.all()
        total = int(sum([(item.product.calories / 100) * item.grams for item in recipeitems]))
        return total

    def get_products(self):
        return "\n".join([p.products for p in self.product.all()])

    def __str__(self):
        return f'id:{self.id}, {self.name}, price:{self.get_total_price}, cals:{self.get_total_calories}'


class Plan(models.Model):
    PLAN_DAYS_CHOICES = [
        ('3d', '3-day plan'),
        ('7d', '7-day plan'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=60, blank=True, null=True, default='Meal Plan')
    type = models.CharField(max_length=12, choices=PLAN_DAYS_CHOICES)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_items(self):
        planitems = self.planitem_set.all()
        total = planitems.count()
        return total

    @property
    def get_total_price(self):
        planitems = self.planitem_set.all()
        total = sum([item.recipe.get_total_price for item in planitems])
        return total

    @property
    def get_total_calories(self):
        planitems = self.planitem_set.all()
        total = sum([item.recipe.get_total_calories for item in planitems])
        return total

    def __str__(self):
        return f'id:{self.id}, {self.type}, owner:{self.user.username}'



class PlanItem(models.Model):
    DAYS_CHOICES = [
        ('1', 'Day 1'),
        ('2', 'Day 2'),
        ('3', 'Day 3'),
        ('4', 'Day 4'),
        ('5', 'Day 5'),
        ('6', 'Day 6'),
        ('7', 'Day 7'),
    ]
    TIME_CHOICES = [
        ('br', 'Breakfast'),
        ('ln', 'Lunch'),
        ('dn', 'Dinner'),
        ('sn', 'Snack'),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True, default=None)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, blank=True, null=True)
    day = models.CharField(max_length=10, choices=DAYS_CHOICES)
    time = models.CharField(max_length=11, choices=TIME_CHOICES, null=True, blank=True)


    def __str__(self):
        return f'id:{self.id} recipe under plan id:{self.plan.id}'