from __future__ import unicode_literals
from passlib.hash import pbkdf2_sha256
from django.db import models
from datetime import date, datetime, timedelta, time
from django.contrib.auth.models import (
    User,
    AbstractBaseUser
)

optional = {
    'null': True,
    'blank': True
}


class PhysicalActivity(models.Model):
    """
        December 22, 2017 - Kwen
        The model where the list of all the kinds of Physical Activity are stored
    """
    name = models.CharField(max_length=255)
    description = models.TextField(default="",**optional)
    percentage_above_basal = models.DecimalField(max_digits=5,decimal_places=2)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Physical Activity"
        verbose_name_plural = "Physical Activities"


class Diet(models.Model):
    """
        December 22, 2017 - Kwen
        The model where the list of all supported diets are stored
    """
    name = models.CharField(max_length=255)
    description = models.TextField(default="",**optional)
    membership_value = models.DecimalField(("Membership Value (Maximum is 1 and Lowest is 0)"),max_digits=8,decimal_places=2,default=0)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Diet"
        verbose_name_plural = "Diets"


class UserSickness(models.Model):
    """
        December 22, 2017 - Kwen
        The model where the list of all supported sickesses are stored
    """
    name = models.CharField(max_length=255)
    description = models.TextField(default="",**optional)
    diet = models.ManyToManyField(Diet)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sickness"
        verbose_name_plural = "Sicknesses"

class UserDescription(models.Model):
    """ 
        December 22, 2017 - Kwen 
        The model stores all the basic user information not including 
        the information needed for the Inference Engine 
    """
    user = models.OneToOneField(User, default=1) #tying this model to the django model
    #first_name = models.CharField(max_length=255)
    #last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    #username =  models.CharField(max_length=255,default = '')
    # password = models.CharField(max_length=255)
    height = models.DecimalField(("Height in meters"),max_digits=8,decimal_places=5)
    weight = models.DecimalField(("Weight in kilograms"),max_digits=8,decimal_places=5)
    physical_activity = models.ForeignKey(PhysicalActivity,default=0)
    #image = models.ImageField(upload_to="media/",default="media/None/no-img.jpg")
    sickness = models.ManyToManyField(UserSickness, blank = True)
    archived = models.BooleanField(default=False)

    def __str__(self):
        #return "{} {}".format(self.first_name, self.last_name)
        return self.user.username
    #def verify_password(self, raw_password):
    #    return pbkdf2_sha256.verify(raw_password,self.password)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

# User.profile = property(lambda u: UserDescription.objects.get_or_create(user=u)[0])
