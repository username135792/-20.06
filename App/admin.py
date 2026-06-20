from django.contrib import admin
from .models import Profile, Application, Review


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'fio', 'birth_date', 'phone')
    search_fields = ('fio', 'user__username')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'transport_type', 'start_date', 'payment_method', 'status', 'created_at')
    list_filter = ('status', 'transport_type', 'payment_method')
    search_fields = ('user__username', 'user__profile__fio')
    list_per_page = 20
    list_editable = ('status',)
    date_hierarchy = 'created_at'


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('application', 'created_at')
    list_filter = ('created_at',)
