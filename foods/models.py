from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from system_user.models import UserDescription
import datetime
from django.contrib.auth.models import (
    User,
    AbstractBaseUser
)

# Create your models here.

optional = {
    'null': True,
    'blank': True
}



class Ingredient(models.Model):
    """
        December 20, 2017 - Kwen
        defines that our model is an object
        This model lists all the ingredients for our food
        class - is a special keyword that indicates taht we are difining an object
        Ingredient - is the name of our model. 
        modesl.Model - means that the Post is a Django Model and should be saved in the database
    """

    name = models.CharField(max_length=200) #text w/ limited number of characters
    description = models.TextField(default="",**optional)
    calories = models.DecimalField(("Calories:"),max_digits=8,decimal_places=2,default=0)
    protein = models.DecimalField(("Protein:"),max_digits=8,decimal_places=2,default=0)
    fat = models.DecimalField(("Fat:"),max_digits=8,decimal_places=2,default=0)
    carbohydrates = models.DecimalField(("Carbohydrates:"),max_digits=8,decimal_places=2,default=0)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Ingredient"
        verbose_name_plural = "Ingredients"

class Diet(models.Model):
    """
        December 20, 2017 - Kwen
        This model lists all the classifications of the foods based on the specific diet
        Food - is the name of our model. 
    """

    diet_type = models.CharField(max_length=200) #text w/ limited number of characters
    notes = models.TextField(default="",**optional)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.diet_type

    class Meta:
        verbose_name = "Diet"
        verbose_name_plural = "Diets"



class DietMembership(models.Model):

    diet = models.ForeignKey(Diet)
    dietmembership=models.DecimalField(("Calories:"),max_digits=8,decimal_places=2,default=0)

    def __str__(self):
        return self.diet.diet_type


class Foods(models.Model):
    """
        December 20, 2017 - Kwen
        defines that our model is an object
        This model lists all the foods containing the ingredients
        class - is a special keyword that indicates taht we are difining an object
        Food - is the name of our model. 
        modesl.Model - means that the Post is a Django Model and should be saved in the database
    """

    name = models.CharField(max_length=200) #text w/ limited number of characters
    notes = models.TextField(default="",**optional)
    calories = models.DecimalField(("Calories:"),max_digits=8,decimal_places=2,default=0)
    protein = models.DecimalField(("Protein"),max_digits=8,decimal_places=2,default=0)
    fat = models.DecimalField(("Fat"),max_digits=8,decimal_places=2,default=0)
    carbohydrates = models.DecimalField(("Carbohydrates"),max_digits=8,decimal_places=2,default=0)
    sodium = models.DecimalField(("Sodium"),max_digits=8,decimal_places=2,default=0)
    fiber = models.DecimalField(("Fiber"),max_digits=8,decimal_places=2,default=0)
    potassium = models.DecimalField(("Potassium"),max_digits=8,decimal_places=2,default=0)
    ingredients = models.ManyToManyField(Ingredient)
    diet = models.ManyToManyField(DietMembership)
    image = models.ImageField(upload_to="media/",default="media/None/no-img.jpg")
    archived = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Food"
        verbose_name_plural = "Foods"


class UsersFoodHistory(models.Model):
    """
        December 20, 2017 - Kwen
        This model guides us the food history of the user
    """
    user = models.ForeignKey(User, default = 0,related_name="users")
    date = models.DateField(("Date"), default=datetime.date.today)
    breakfast = models.ForeignKey(Foods, related_name = "Breakfast", **optional)
    lunch = models.ForeignKey(Foods, related_name = "Lunch", **optional)
    dinner = models.ForeignKey(Foods, related_name = "Dinner", **optional)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return str(self.date)
    
    class Meta:
        verbose_name = "User's Food History"
        verbose_name_plural = "User's Food History"