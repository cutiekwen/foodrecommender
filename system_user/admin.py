from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from django.contrib.auth.models import (
    User,
    AbstractBaseUser
)
from system_user.models import (UserDescription,
        UserSickness,
        PhysicalActivity, 
        Diet
    )


# Imports needed for overriding the admin interface
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


# Define an 'inline' userdescription, Inline meaning pwede nimo I stack sa isa ka admin page

class UserDescriptionInline(admin.StackedInline):
    model = UserDescription
    can_delete = False
    verbose_name_plural = 'UserDescription'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserDescriptionInline,)

class DietAdmin(admin.ModelAdmin):
    model = Diet
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class UserSicknessAdmin(admin.ModelAdmin):
    model = UserSickness
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class PhysicalActivityAdmin(admin.ModelAdmin):
    model = PhysicalActivity
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class UserDescriptionAdmin(admin.ModelAdmin):
    model = UserDescription
#     list_display = ['first_name', 'last_name', 'gender','username','password']
#     list_filter = ('archived',)
#     list_display_links = ('first_name', 'last_name', 'gender','username','password')
#     search_fields = ('first_name', 'last_name', 'username')
#     list_per_page = 25
#     #inlines = [UserSicknessTabularInline]
#     list_filter = ('archived',)
    
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False



# Unregister ang default na user interface
admin.site.unregister(User)
# Register ang bago na User Interface
admin.site.register(User, UserAdmin)


admin.site.register(UserSickness,UserSicknessAdmin)
admin.site.register(PhysicalActivity,PhysicalActivityAdmin)
admin.site.register(Diet,DietAdmin)