from django.contrib import admin

from user_actions import models as review_models


@admin.register(review_models.Review)
class ReviewAdminSite(admin.ModelAdmin):
    site_header = 'Пользовательские действия'
    list_display = ('text', 'created_at')
    list_filter = ('created_at',)
