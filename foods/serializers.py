from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from django.conf import settings
from random import randint
from rest_framework import serializers
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

from foods.models import(
    Ingredient,
    Diet,
    Foods,
    UsersFoodHistory,
)



class UsersFoodHistorySerializer(serializers.ModelSerializer):
    """
        This class is for serializing sickness
    """

    class Meta:
        model = UsersFoodHistory 
        fields = '__all__'


class FoodSearchSerializer(serializers.ModelSerializer):
    """
        This class is for serializing sickness
    """

    class Meta:
        model = Foods 
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    """
        This class is for serializing sickness
    """

    class Meta:
        model = Ingredient 
        fields = '__all__'


class DietSerializer(serializers.ModelSerializer):
    """
        This class is for serializing sickness
    """

    class Meta:
        model = Diet 
        fields = '__all__'


class FoodsSerializer(serializers.ModelSerializer):
    """
        This class is for serializing sickness
    """

    class Meta:
        model = Foods 
        fields = '__all__'


class TotalBreakfast(object):
    """
        This class is used to initialize the BMI value

    """
    def __init__(self,breakfast_total):
        self.breakfast_total = breakfast_total

class TotalBreakfastSerializer(serializers.Serializer):
    """
        This class is used for serailizing the BMI of the user
    """

    breakfast_total = serializers.IntegerField()

class TotalLunch(object):
    """
        This class is used to initialize the BMI value

    """
    def __init__(self,lunch_total):
        self.lunch_total = lunch_total

class TotalLunchSerializer(serializers.Serializer):
    """
        This class is used for serailizing the BMI of the user
    """

    lunch_total = serializers.IntegerField()

class TotalDinner(object):
    """
        This class is used to initialize the BMI value

    """
    def __init__(self,dinner_total):
        self.dinner_total = dinner_total

class TotalDinnerSerializer(serializers.Serializer):
    """
        This class is used for serailizing the BMI of the user
    """

    dinner_total = serializers.IntegerField()


class FavBfast(object):
    """
        This class is used to initialize the BMI value

    """
    def __init__(self,fav_bfast):
        self.fav_bfast = fav_bfast

class FabBfatSerializer(serializers.Serializer):
    """
        This class is used for serailizing the BMI of the user
    """

    fav_bfast = serializers.CharField()
