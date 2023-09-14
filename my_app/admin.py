from django.contrib import admin

from my_app import models as my_app_models


@admin.register(my_app_models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'duration', 'director')
    list_filter = ('created_at', 'duration')
    search_fields = ('title', 'description')


@admin.register(my_app_models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('created_at',)
    search_fields = ('name',)
