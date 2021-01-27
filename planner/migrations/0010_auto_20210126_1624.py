# Generated by Django 3.1.5 on 2021-01-26 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0009_auto_20210126_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planitem',
            name='grams',
        ),
        migrations.RemoveField(
            model_name='planitem',
            name='product',
        ),
        migrations.AddField(
            model_name='plan',
            name='name',
            field=models.CharField(blank=True, default='Meal Plan', max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='planitem',
            name='recipe',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='planner.recipe'),
        ),
    ]