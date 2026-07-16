from django.contrib import admin

# Register your models here.
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["subject", "sender", "recipient", "is_read", "is_archived", ""
    "sent_at"]
    list_filter = ["is_read", "is_archived", "sent_at"]
    search_fields = ["subject", "body", "sender__username", "recipient__username"]