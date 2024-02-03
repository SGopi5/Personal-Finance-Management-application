from django.contrib import admin
from app.models import *

from django.contrib import admin
from .models import Expense

class ReadOnlyExpenseAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Date_of_Expence', 'Amount', 'Category', 'created_by', 'created_at')
    list_filter = ('Category', 'Date_of_Expence')
    search_fields = ('Name', 'Description')

    def has_add_permission(self, request):
        return False  # Disable the "Add" button

    def has_change_permission(self, request, obj=None):
        return False  # Disable the "Change" button

    def has_delete_permission(self, request, obj=None):
        return False  # Disable the "Delete" button

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']  # Disable the "Delete selected" action
        return actions

admin.site.register(Expense , ReadOnlyExpenseAdmin)
