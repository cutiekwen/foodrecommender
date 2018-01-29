from django.shortcuts import render
from PIL import Image
# Create your views here.

from django.db.models import Q
from django.core import serializers
from django.shortcuts import get_object_or_404 # checks if an objects exists of not
from rest_framework import generics
from rest_framework.fields import empty
from rest_framework.views import APIView  # returns API Data
from rest_framework.response import Response # returns response


from foods.models import (
        Ingredient, 
        Diet, 
        Foods,
        UsersFoodHistory,
    )

from foods.serializers import(
        UsersFoodHistorySerializer,
        FoodSearchSerializer,
        IngredientSerializer,
        DietSerializer,
        FoodsSerializer,
        TotalBreakfast,
        TotalBreakfastSerializer,
        TotalLunch,
        TotalLunchSerializer,
        TotalDinner,
        TotalDinnerSerializer,
    )

from rest_framework.permissions import(
    AllowAny, 
    IsAuthenticated, 
    IsAdminUser, 
    IsAuthenticatedOrReadOnly,
)

class SuggestFood(APIView):
    pass

class FoodHistory(APIView):

    def get(self,request,pk):
        """ 
            This function will get all the user's food history in our database

            Returns: A json response of all the user's food history in our database

        """
        try:
            """
                The variables below are the initalization for the JSON data to be sent
                We made our own JSON Data
            """
            final_data = {} 
            breakfast = {}
            lunch = {}
            dinner = {}
            food_history = UsersFoodHistory.objects.filter(user=pk).order_by('date')
            for food in food_history:
                try: 
                   
                    breakfast = {
                        'id' : food.breakfast.id,
                        'name' : food.breakfast.name,
                        'calories' : food.breakfast.calories,
                        'protein' : food.breakfast.protein,
                        'carbohydrates': food.breakfast.carbohydrates,
                        'fats' : food.breakfast.fat ,
                        'image' : food.breakfast.image.url
                    }
                except Exception as a:
                    print str(a)
                    breakfast = {}
                
                try:
                    lunch = {
                        'id' : food.lunch.id,
                        'name' : food.lunch.name,
                        'calories' : food.lunch.calories,
                        'protein' : food.lunch.protein,
                        'carbohydrates': food.lunch.carbohydrates,
                        'fats' : food.lunch.fat ,
                        'image' : food.lunch.image.url
                    }
                except Exception as b:
                    print str(b)
                    lunch = {}

                try:    
                    dinner = {
                        'id' : food.dinner.id,
                        'name' : food.dinner.name,
                        'calories' : food.dinner.calories,
                        'protein' : food.dinner.protein,
                        'carbohydrates': food.dinner.carbohydrates,
                        'fats' : food.dinner.fat,
                        'image' : food.dinner.image.url  
                    }
                except Exception as c:
                    print str(c)
                    dinner = {}

                final_data [food.id] = {
                    'id' : food.id,
                    'date' : food.date,
                    'archived': food.archived,
                    'breakfast' : breakfast ,
                    'lunch' : lunch,
                    'dinner' : dinner,  
                }
            return Response(final_data)
        except Exception as e:
            print str(e)
            return Response({'Error':'You do not have any food history at the moment.'})
        
        
        
        
        

from itertools import chain #used for comination of queries on two different base models

class FoodSearch(APIView):

    def get(self, request,search):
        """ 
            This function will return a list of foods based from the 
            food name or the ingredient name.

            Args: search - The value of the food/ ingredient to be searched

            Returns: A json response of all the foods/ingredients with that 
            matches the search value

        """
        foods = Foods.objects.filter(
            name__icontains=search,archived=False
        )

        ingredients = Ingredient.objects.filter(
            name__icontains=search,archived = False
        )

        foods_serializer = FoodSearchSerializer(
            foods,many=True
        )

        ingredients_serializer = IngredientSerializer(
            ingredients, many=True
        )

        data = { 'Foods': foods_serializer.data,
            'Ingredients':ingredients_serializer.data,
          } 
        
        return Response(data)

class GetFood(APIView):

    def get(self,request,pk):
        """ 
            This function will get the food of the corresponding ID in the database

            Returns: A json response of all the matched food

        """
        food = Foods.objects.filter(id=pk)
        serializer = FoodsSerializer(food,many=True)
        return Response(serializer.data)


class AllFood(APIView):

    def get(self,request):
        """ 
            This function will get all  the foods in the database

            Returns: A json response of all the matched food

        """
        food = Foods.objects.all()
        serializer = FoodsSerializer(food,many=True)
        return Response(serializer.data)

from django.db.models import Count

class GetFavoriteFood(APIView):

    def get(self,request, pk):
        """ 
            This function will get all  the foods in the database

            Returns: A json response of all the matched food

        """
        try:
            users = UsersFoodHistory.objects.filter(user = pk)
            breakfast = UsersFoodHistory.objects.filter(user = pk).values('breakfast').annotate(total=Count('breakfast')).order_by('-total')
            lunch = UsersFoodHistory.objects.filter(user = pk).values('lunch').annotate(total=Count('lunch')).order_by('-total')
            dinner = UsersFoodHistory.objects.filter(user = pk).values('dinner').annotate(total=Count('dinner')).order_by('-total')
            
            favorite_breakfast = Foods.objects.get(
                id=breakfast[0]['breakfast'])
           
            favorite_breakfast_serializer = FoodsSerializer(favorite_breakfast)

            favorite_breakfast_total = TotalBreakfast(breakfast[0]['total'])
            
            favorite_breakfast_total_serializer = TotalBreakfastSerializer(favorite_breakfast_total)

            favorite_lunch = Foods.objects.get(
                id=lunch[0]['lunch'])
            favorite_lunch_serializer = FoodsSerializer(favorite_lunch)
            favorite_lunch_total = TotalLunch(lunch[0]['total'])
            favorite_lunch_total_serializer = TotalLunchSerializer(favorite_lunch_total)

            favorite_dinner = Foods.objects.get(
                id=dinner[0]['dinner'])
            
            favorite_dinner_serializer = FoodsSerializer(favorite_dinner)
            
            favorite_dinner_total = TotalDinner(dinner[0]['total'])
            favorite_dinner_total_serializer = TotalDinnerSerializer(favorite_dinner_total)
        
        
            data = {
            'Favorite Breakfast': favorite_breakfast_serializer.data,
            'Favorite Breakfast Total' : favorite_breakfast_total_serializer.data,
            'Favorite Lunch': favorite_lunch_serializer.data,
            'Favorite Lunch Total' : favorite_lunch_total_serializer.data,
            'Favorite Dinner' : favorite_dinner_serializer.data,
            'Favorite Dinner Total': favorite_dinner_total_serializer.data
            }

            return Response(data)

        except Exception as e:
            print e
            return Response({'Error':'You do not have any favorite foods at the moment.'})


class UpdateFoodHistory(generics.RetrieveUpdateAPIView):  
    """ 
        This class will update a user based on the userid
        lookup_field will automatically get the detail of the current user
    """

    serializer_class = UsersFoodHistorySerializer 
    permission_classes = (AllowAny,)
    lookup_field = 'pk'
    def get_queryset(self):
        foodhistoryid = int(self.kwargs["pk"]) #values passed from urls
        return UsersFoodHistory.objects.filter(id=foodhistoryid)

class SearchFoodHistory(APIView):

    def get(self, request,pk,date):
        """ 
            This function will return a list of foods based from the 
            food name or the ingredient name.

            Args: search - The value of the food/ ingredient to be searched

            Returns: A json response of all the foods/ingredients with that 
            matches the search value

        """
        try:
            foods = UsersFoodHistory.objects.get(
                user=pk , date=date
            )
            serializer = UsersFoodHistorySerializer(foods)
            return Response(serializer.data)
        except Exception as e:
            #print str(e)
            return Response({'No results found.'})

class NewFoodHistory(generics.CreateAPIView):
    """
        This class will create a new food history
        lookup_field will automatically get the detail of the newly added food
    """
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    serializer_class = UsersFoodHistorySerializer    
    
    def get_queryset(self):
        return UsersFoodHistory.objects.all()

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
