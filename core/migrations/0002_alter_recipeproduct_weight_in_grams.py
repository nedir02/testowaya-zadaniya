# Generated by Django 5.0.1 on 2024-01-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeproduct',
            name='weight_in_grams',
            field=models.IntegerField(null=True),
        ),
    ]
