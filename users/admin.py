from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_dispay= ["user", "role", "department", "phone"]
    list_filter = ["user", "department"]
    search_fields = ["user__username", "user__email", "department"]