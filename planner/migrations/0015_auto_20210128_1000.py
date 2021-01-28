# Generated by Django 3.1.5 on 2021-01-28 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0014_auto_20210127_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='type',
            field=models.CharField(choices=[('3d', '3-day plan'), ('7d', '7-day plan')], max_length=255),
        ),
        migrations.AlterField(
            model_name='planitem',
            name='day',
            field=models.CharField(choices=[('1', 'Day 1'), ('2', 'Day 2'), ('3', 'Day 3'), ('4', 'Day 4'), ('5', 'Day 5'), ('6', 'Day 6'), ('7', 'Day 7')], max_length=255),
        ),
        migrations.AlterField(
            model_name='planitem',
            name='recipe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planner.recipe'),
        ),
        migrations.AlterField(
            model_name='planitem',
            name='time',
            field=models.CharField(blank=True, choices=[('br', 'Breakfast'), ('ln', 'Lunch'), ('dn', 'Dinner'), ('sn', 'Snack')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='grams',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipeitem',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='planner.product'),
        ),
    ]