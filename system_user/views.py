from django.shortcuts import render

# Create your views here.
from passlib.hash import pbkdf2_sha256
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate
import base64
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core import serializers
from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404 # checks if an objects exists of not
from rest_framework import (
    generics,
    mixins, 
    exceptions, 
    status
    )
from rest_framework.fields import empty
from rest_framework.views import APIView  # returns API Data
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response # returns response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework import authentication
from rest_framework.permissions import(
    AllowAny, 
    IsAuthenticated, 
    IsAdminUser, 
    IsAuthenticatedOrReadOnly,
)

from rest_framework.authentication import (
    BaseAuthentication,
    SessionAuthentication
)

from math import floor

from system_user.models import (
        UserDescription,
        UserSickness,
        PhysicalActivity, 
    )

from system_user.serializers import (
        SicknessSerializer,
        PhysicalActivitySerializer,
        UserDescriptionSerializer,
        BMISerializer,
        BMIResultSerializer,
        DBWSerializer,
        TERSerializer,
        ProteinSerializer,
        FatsSerializer,
        CarbsSerializer,
        BMI,
        BMIResult,
        DBW,
        TER,
        Protein,
        Fats,
        Carbs,
        UserSerializer,
        UserLoginSerializer,
    )

class GetAllSickness(APIView):

    def get(self,request):
        """ 
            This function will get all the sicknesses from our database

            Returns: A json response of all the sicknesses in our database

        """
        sickness_result = UserSickness.objects.all()
        serializer = SicknessSerializer(sickness_result,many=True)
        return Response(serializer.data)

class GetAllPhysicalActivites(APIView):

    def get(self,request):
        """ 
            This function will get the different physical activities from our database

            Returns: A json response of all the physical activities in our database

        """
        activities_result = PhysicalActivity.objects.all()
        serializer = PhysicalActivitySerializer(activities_result,many=True)
        return Response(serializer.data)

class GetUserInformation(APIView):

    def get(self,request,userid):
        """
            This function will display all the user information based on the
            user's primary key

            Args: value- The specific user that accesses the system

            Returns: A json response with the user's information
        """

        current_user = UserDescription.objects.filter(
            user=userid)

        user_description = User.objects.filter(id=userid)


        current_user_serializer = UserDescriptionSerializer(
            current_user,many=True)
        user_serializer = UserSerializer(
            user_description, many=True
        )

        """
            Calculating the BMI of the user
        """
        height = float(current_user.first().height)
        weight = float(current_user.first().weight)
        bmi_height = float(height * height)
        bmi_result = float(round(weight / bmi_height))
        
        """
            Classifying the BMI of the User
        """

        if(bmi_result<18.5):
            bmi_checker = "Underweight"
        elif(bmi_result>=18.5 and bmi_result<=22.9):
            bmi_checker = "Normal"
        elif(bmi_result>=23 and bmi_result<=26.9):
            bmi_checker = "Overwieght"
        elif(bmi_result>=27):
            bmi_checker = "Obese"
            
        """
            Calculating the Desired Body Weight using Tannhauser's Method
        """
        dbw_height = float(height * 100)
        dbw = float((dbw_height -100) - (0.1 *(dbw_height-100)))
        dbw = float(round(dbw,2))
        """
            Getting the User's precentage above Basal
        """
        users_physical_activity = (current_user.first().physical_activity.id)
        match_physical_activity = PhysicalActivity.objects.filter(
            id=users_physical_activity)
        percentage_above_basal = float(match_physical_activity.first().percentage_above_basal)

        """
            Calculating the Basal Metabolic Rate
        """
        
        bmr = float(1*dbw*24) 
        bmr = float(str(round(bmr)))
        #print ("bmr: ",bmr)
        
        """
            Calculating the Percentage of Physical Activity of the User
        """

        pa = float(bmr * (percentage_above_basal / 100))
        pa = float(str(round(pa)))
        #print ("pa: ",pa)

        """
            Calculating the Specific Dynamic Actions of Foods
        """

        sda = (bmr + pa) * 0.1
        sda = float(str(round(sda)))
        #print ("sda: ",sda)

        """
            Calculating the Total Energy Requirements
        """

        ter = bmr + pa + sda 
        ter = int(50 * round(float(ter)/50)) #round off to nearest 50
        #print ("ter: ",ter)

        """
            Calculating the Recommended Protein Intake and round to the nearest 5
        """

        protein_intake = int(ter * 0.12)/4
        #print ("protein_intake: ",protein_intake)
        protein_intake = floor(protein_intake/5)
        #print ("protein_intake: ",protein_intake)

        if(protein_intake%2==0):
            protein_intake += 1
        
        protein_intake = protein_intake*5
        #print ("protein_intake: ",protein_intake)

        """
            Calculating the Recommended Fat Intake and round to the nearest 5
        """

        fats_intake = (ter * 0.25)/9
        #print ("fats_intake: ",fats_intake)
        fats_intake = floor(fats_intake/5)
        #print ("fats_intake: ",fats_intake)

        if(fats_intake%2==0):
            fats_intake += 1
        
        fats_intake = fats_intake*5
        #print ("fats_intake: ",fats_intake)

        """
            Calculating the Recommended Carbohydrate Intake and round to the nearest 5
        """

        carbs_intake = (ter * 0.60) / 4
        #print ("carbs_intake: ",carbs_intake)
        carbs_intake = floor(carbs_intake/5)
        #print ("carbs_intake: ",carbs_intake)

        if(carbs_intake%2==0):
            carbs_intake +=1
        
        carbs_intake = carbs_intake*5
        #print ("carbs_intake: ",carbs_intake)

        """
            Converting Excess Calories to Carbohydrates
        """

        carbohydrates_calories = carbs_intake * 4
        protein_calories = protein_intake * 4
        fats_calories = fats_intake * 9
        excess_calories = (ter - (
            carbohydrates_calories + protein_calories + fats_calories))
        
        excess_calories = excess_calories / 4
        carbs_intake = carbs_intake + excess_calories

        bmi_to_serialize = BMI(bmi_result)
        bmi_serializer = BMISerializer(bmi_to_serialize)
        
        bmi_result_to_serialize = BMIResult(bmi_checker)
        bmi_result_serializer = BMIResultSerializer(bmi_result_to_serialize)
        
        dbw_to_serialize = DBW(dbw)
        dbw_serializer = DBWSerializer(dbw_to_serialize)
        
        ter_to_serialize = TER(ter)
        ter_serializer = TERSerializer(ter_to_serialize)
        
        protein_to_serialize = Protein(protein_intake)
        protein_serializer = ProteinSerializer(protein_to_serialize)
        
        fats_to_serialize = Fats(fats_intake)
        fats_serializer = FatsSerializer(fats_to_serialize)
        
        carbs_to_serialize = Carbs(carbs_intake)
        carbs_serializer = CarbsSerializer(carbs_to_serialize)

        data = { 'User Information': current_user_serializer.data,
            'User Information Profile':user_serializer.data,
            'Users Body Mass Index': bmi_serializer.data,
            'Users BMI Results': bmi_result_serializer.data,
            'Users Desired Body Weight in kilograms': dbw_serializer.data,
            'Users Total Energy Requirements': ter_serializer.data,
            'Users Protein Intake (in grams)': protein_serializer.data,
            'Users Fats Intake (in grams)': fats_serializer.data,
            'Users Carbohydrate Intake (in grams)': carbs_serializer.data, } 
        return Response(data)  

class UpdateUser(generics.RetrieveUpdateAPIView):  
    """ 
        This class will update a user based on the userid
        lookup_field will automatically get the detail of the current user
    """
    permission_classes = (AllowAny,)
    lookup_field = 'id'
    serializer_class = UserSerializer    
    def get_queryset(self):
        return User.objects.all()

class UpdateUser2(generics.RetrieveUpdateAPIView):  
    """ 
        This class will update a user based on the userid
        lookup_field will automatically get the detail of the current user
    """
    permission_classes = (AllowAny,)
    lookup_field = 'id'
    serializer_class = UserDescriptionSerializer    
    def get_queryset(self):
        return UserDescription.objects.all()

class CreateUser(generics.CreateAPIView):  
    """
        This class will create a new user
        lookup_field will automatically get the detail of the current user
    """
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer    
    
    def get_queryset(self):
        return User.objects.all()

    def perform_create(self, serializer):
       
        if serializer.is_valid():
            serializer.save()

class CreateUser2(generics.CreateAPIView):  
    """
        This class will create a new user
        lookup_field will automatically get the detail of the current user
    """
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    serializer_class = UserDescriptionSerializer    
    
    def get_queryset(self):
        return UserDescription.objects.all()

    def perform_create(self, serializer):
       
        if serializer.is_valid():
            serializer.save()

class Login(APIView):
    """
        This class verifies if the user is in the database and will output the userid of the user
        the get_user_model() is the Django Auth model
        AllowAny - permission_classes because everyone could be able to login
    """

    model = get_user_model()
    permission_classes = (AllowAny,)

   
    def post(self, request, format=None):
        """
            This method converts serializer inputs and stores it into a variable to be checked by
            the built-in authenticate function of Django then using the username, a query is made
            in order to get the userid of the user
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            #serializer.save() - for saving serializer
            #username = request.POST.get['username']
            #password = request.POST.get['password']    
            username = serializer.data['username']
            password = serializer.data['password']
            #print (username)

            user = authenticate(username=username, password=password)
            #print("userisnotnone")
            if user is not None:
                #print("unilever")

                if user.is_active:
                    get_user_id = User.objects.filter(
                    username=username)
                    #print get_user_id.first().id
                    return Response({"userid": get_user_id.first().id})
                #    print("successss")  
                       
            return Response({"Invalid Credentials"})
        return Response({"Invalid Credentials"})







"""
This is a sample class of a combination between the ListAPIView combined with MixIns model
this is done because in the LISTAPIView the only method allowed is GET, which is why
with the use of the Mixins in API View, we will program the REST API to allow other methods 
like POST, PUT, PATCH, etc.

class CreateUser(mixins.CreateModelMixin, generics.ListAPIView):  
    CreateModelMixin can be changed depending on the method that you want to add

    lookup_field = 'id'
    serializer_class = UserSerializer    

    def get_queryset(self):
        return UserDescription.objects.all()

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        serializer.save()

    def post(self, request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    another example would be the put and patch method, but the mixin would also change

    def put(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request,*args,**kwargs)
"""
