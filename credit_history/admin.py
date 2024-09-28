from django.contrib import admin

from .models import CreditHistory

@admin.register(CreditHistory)
class HistoryAdmin(admin.ModelAdmin):
  list_display = ('date', 'old_status', 'new_status') 
  list_filter = ('date',)
  search_fields = ('old_status', 'new_status')