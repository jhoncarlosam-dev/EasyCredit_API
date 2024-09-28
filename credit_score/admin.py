from django.contrib import admin
from .models import CreditScore

class CreditScoreAdmin(admin.ModelAdmin):
    list_display = ('score', 'calculation_date')
    list_filter = ('calculation_date',)
    search_fields = ('score',)

admin.site.register(CreditScore, CreditScoreAdmin)