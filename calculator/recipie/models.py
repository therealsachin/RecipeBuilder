from __future__ import unicode_literals

from django.db import models


class Recipe(models.Model):
    name = models.TextField(null=False)
    recipe_text = models.TextField()


class Ingredient(models.Model):
    name = models.TextField(null=False)
    protein = models.IntegerField()
    fibre = models.IntegerField()
    carbs = models.IntegerField()
    fat = models.IntegerField()


class NutritionalFactor(models.Model):
    name = models.TextField(null=False)


class IngredientNutritionalValue(models.Model):
    ingredient = models.ForeignKey(to=Ingredient)
    nutritional_factor = models.ForeignKey(to=NutritionalFactor)
