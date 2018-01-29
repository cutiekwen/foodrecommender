from django.contrib import admin

# Register your models here.
from knowledgebased.models import (
    RulesMembership,
    WorkingMemory,
    Rules
)

class RulesMembershipAdmin(admin.ModelAdmin):
    model = RulesMembership
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class RulesAdmin(admin.ModelAdmin):
    model = Rules
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

class WorkingMemoryAdmin(admin.ModelAdmin):
    model = WorkingMemory
    def has_delete_permission(self, request, obj=None):
        """
                This function disables the delete action of the django-admin
        """
        return False

admin.site.register(RulesMembership,RulesMembershipAdmin)
admin.site.register(Rules,RulesAdmin)
admin.site.register(WorkingMemory,WorkingMemoryAdmin)