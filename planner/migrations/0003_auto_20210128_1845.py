# Generated by Django 3.1.5 on 2021-01-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_auto_20210128_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planitem',
            name='time',
            field=models.CharField(blank=True, choices=[('br', 'Завтрак'), ('ln', 'Обед'), ('dn', 'Ужин'), ('sn', 'Перекус')], max_length=255, null=True),
        ),
    ]
