from passlib.hash import pbkdf2_sha256
from django.contrib.gis.geos import fromstr
from django.contrib.gis.measure import D
from django.conf import settings
from random import randint
from rest_framework import serializers
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.db.models import Q 
import crypt
from rest_framework.serializers import(
    EmailField,
    ValidationError,
    CharField,
    DateField,
    DecimalField,
    PrimaryKeyRelatedField,
    ImageField
)

from system_user.models import (
        UserDescription,
        UserSickness,
        PhysicalActivity, 
    )

class SicknessSerializer(serializers.ModelSerializer):
    """
        This class is for serializing sickness
    """

    class Meta:
        model = UserSickness 
        fields = '__all__'

class PhysicalActivitySerializer(serializers.ModelSerializer):
    """
        This class is for serializing physical activity
    """

    class Meta:
        model = PhysicalActivity 
        fields = '__all__'


class UserDescriptionSerializer(serializers.ModelSerializer):
    """
        This class is for serializing User Description
    
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    gender = serializers.CharField(max_length=6)
    birthday = serializers.DateField(("Birthday"))
    username =  serializers.CharField(max_length=255,default = '')
    password = serializers.CharField(max_length=255)
    height = serializers.DecimalField(max_digits=5, decimal_places=2)
    weight = serializers.DecimalField(max_digits=5, decimal_places=2)
    physical_activity =  PrimaryKeyRelatedField(queryset=PhysicalActivity.objects.all())
    image = serializers.ImageField(ImageField(max_length=None, allow_empty_file=False, use_url="media/"))
    sickness = serializers.PrimaryKeyRelatedField(queryset=UserSickness.objects.all(),many=True)
    archived = serializers.BooleanField(default=False)
    """


    class Meta:
        model = UserDescription
        fields = ('user','gender','height','weight','physical_activity','sickness')
        read_only_fields = ('archived',)
    
class UserSerializer(serializers.ModelSerializer):
    """
        This class is used for serailizing the User Information
    """

    def create (self,validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('id','username','password','first_name','last_name','email','is_active',)
        #extra_kwargs = {'password':{'write_only':True}}

class BMI(object):
    """
        This class is used to initialize the BMI value

    """
    def __init__(self,bmi_value):
        self.bmi_value = bmi_value

class BMISerializer(serializers.Serializer):
    """
        This class is used for serailizing the BMI of the user
    """

    bmi_value = serializers.FloatField()

class BMIResult(object):
    """
        This class is used to initialize the BMI Result value

    """
    def __init__(self,bmi_value):
        self.bmi_value = bmi_value

class BMIResultSerializer(serializers.Serializer):
    """
        This class is used for serailizing the BMI Result of the user
    """

    bmi_value = serializers.CharField()

class DBW(object):
    """
        This class is used to initialize the BMI Result value

    """
    def __init__(self,dbw_value):
        self.dbw_value = dbw_value

class DBWSerializer(serializers.Serializer):
    """
        This class is used for serailizing the Desired Body Weight of the user
    """

    dbw_value = serializers.FloatField()

class TER(object):
    """
        This class is used to initialize the Total Energy Requirement value

    """
    def __init__(self,ter_value):
        self.ter_value = ter_value

class TERSerializer(serializers.Serializer):
    """
        This class is used for serailizing the Total Energy Requirement of the user
    """

    ter_value = serializers.FloatField()

class Protein(object):
    """
        This class is used to initialize the Protein value

    """
    def __init__(self,protein_requirement):
        self.protein_requirement = protein_requirement

class ProteinSerializer(serializers.Serializer):
    """
        This class is used for serailizing the Protein intake of the user
    """

    protein_requirement = serializers.FloatField()

class Fats(object):
    """
        This class is used to initialize the Fats value

    """
    def __init__(self,fats_requirement):
        self.fats_requirement = fats_requirement

class FatsSerializer(serializers.Serializer):
    """
        This class is used for serailizing the Fats Intake of the user
    """

    fats_requirement = serializers.FloatField()

class Carbs(object):
    """
        This class is used to initialize the Carbs value

    """
    def __init__(self,carbs_requirement):
        self.carbs_requirement = carbs_requirement

class CarbsSerializer(serializers.Serializer):
    """
        This class is used for serailizing the Carbohydrates Intake of the user
    """

    carbs_requirement= serializers.FloatField()

class CreateUserSerializer(serializers.ModelSerializer):
    """
        This class is used for serailizing the login views
    """
    password = serializers.CharField(write_only=True)
    
    #we override Create method

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
    
    class Meta:
        model = get_user_model()
        fields = ['username','password']
        extra_kwargs = {'password':{'write_only':True}}

class UserLoginSerializer(serializers.ModelSerializer):
    """
        This class is used for serailizing the login views
    """
    username = serializers.CharField()
    password = serializers.CharField()   


    class Meta:
        model = User
        fields = ['username','password']



    
