from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class recipe(models.Model):

    recipe_name = models.CharField(max_length=100)
    people_served = models.TextField(blank=True)
    calories = models.TextField(blank=True)
    difficulty = models.TextField(blank=True)
    ingredients = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    age = models.CharField(max_length=20, blank=True)
    category = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=50, blank=True)
class gen_ins(models.Model):
    instructions=models.TextField()
    food_items=models.TextField()
    mal_ins=models.TextField()
    age=models.CharField(max_length=20,null=True)

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    proteins = models.FloatField()
    vitamins = models.FloatField()
    minerals = models.FloatField()
    carbohydrates = models.FloatField()
    fats = models.FloatField()
    calories = models.FloatField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=15, choices=[('Male', 'Male'), ('Female', 'Female')])
    def _str_(self):
        return self.user.username

class BMIHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bmi_value = models.FloatField()
    predicted_bmi = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)