from django.contrib import admin
from .models import CreateUsers

@admin.register(CreateUsers)
class EmployeesAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'credit_score']
  search_fields = ['name']