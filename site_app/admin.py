from django.contrib import admin
from .models import FeatureCard


@admin.register(FeatureCard)
class FeatureCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'description',)
    list_filter = ('title',)
