# Generated by Django 3.1.5 on 2021-01-26 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0010_auto_20210126_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plan',
            name='recipes',
        ),
    ]
