from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.admin import UserAdmin

from foods.models import (Foods,
        Ingredient,
        Diet, 
        UsersFoodHistory,
        DietMembership
    )



class DietMembershipAdmin(admin.ModelAdmin):
    model = DietMembership
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False


class DietTypeAdmin(admin.ModelAdmin):
    model = Diet
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class IngredientsAdmin(admin.ModelAdmin):
    model = Ingredient
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class FoodsAdmin(admin.ModelAdmin):
    model = Foods
    list_display = ['name', 'calories', 'protein','fat','carbohydrates']
    list_filter = ('archived','name','calories','protien','fat','carbohydrates')
    list_display_links = ('name', 'calories', 'protein','fat','carbohydrates')
    search_fields = ('name', 'notes','ingredients')
    list_per_page = 25
    list_filter = ('archived',)
    

    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class FoodHistoryAdmin(admin.ModelAdmin):
    model = UsersFoodHistory
    list_display = ['user', 'date', 'breakfast','lunch','dinner']
    list_filter = ('archived','date','user','breakfast','lunch','dinner')
    list_display_links = ('user', 'date', 'breakfast','lunch','dinner')
    search_fields = ('breakfast', 'lunch','dinner')
    list_per_page = 25
    list_filter = ('archived',)
    

    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

admin.site.register(DietMembership,DietMembershipAdmin)
admin.site.register(Foods,FoodsAdmin)
admin.site.register(Ingredient,IngredientsAdmin)
admin.site.register(Diet,DietTypeAdmin)
admin.site.register(UsersFoodHistory,FoodHistoryAdmin)