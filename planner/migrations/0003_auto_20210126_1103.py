# Generated by Django 3.1.5 on 2021-01-26 08:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20210126_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planitem',
            name='day',
            field=models.CharField(choices=[('1', 'Day 1'), ('2', 'Day 2'), ('3', 'Day 3'), ('4', 'Day 4'), ('5', 'Day 5'), ('6', 'Day 6'), ('7', 'Day 7')], default=django.utils.timezone.now, max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planitem',
            name='time',
            field=models.CharField(blank=True, choices=[('br', 'Breakfast'), ('ln', 'Lunch'), ('dn', 'Dinner'), ('sn', 'Snack')], max_length=2, null=True),
        ),
    ]