from django.contrib import admin

# Models
from .models import Project, Category

# Lists for project values

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'status', 'category', 'start_date', 'end_date')
    list_filter = ('status', 'category')
    search_fields = ('name', 'description', 'stakeholders')

# Categories managed by admins through admin panel

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)