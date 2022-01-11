from django.contrib import admin

# Register your models here.

from investment.models import Investment,InvestmentState

@admin.register(Investment,InvestmentState)

class GenericAdmin(admin.ModelAdmin):
    pass