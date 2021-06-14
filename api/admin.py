from django.contrib import admin
from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'difficulty', 'created_at')
    ordering = ['id']


admin.site.register(Recipe, RecipeAdmin)
