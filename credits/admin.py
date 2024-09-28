from django.contrib import admin

from .models import CreateCredit

# Register your models here.
@admin.register(CreateCredit)
class CreateCreditAdmin(admin.ModelAdmin):
  list_display = ['id', 'name', 'status']
  search_fields = ['name']