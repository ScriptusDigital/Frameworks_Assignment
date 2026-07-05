from django.contrib import admin

# Register your models here.
from .models import Project, Category

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'category', 'start_date', 'end_date')
    list_filter = ('status', 'category')
    search_fields = ('name', 'description', 'stakeholders')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)