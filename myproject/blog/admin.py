from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name','description','created_at']