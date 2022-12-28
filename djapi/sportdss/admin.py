from django.contrib import admin
from .models import BaseCategory, Service, Object, Managment

# admin.site.register(BaseCategory)
# admin.site.register(Service)
# admin.site.register(Object)
# 
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'long_name', 'address', 'category', 'display_service', 'display_sportsection')


@admin.register(BaseCategory)
class BaseCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'newname')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'descriprion', 'category')

@admin.register(Managment)
class ManagmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_title')