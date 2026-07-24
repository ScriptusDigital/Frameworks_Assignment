from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Storing messages sent between users
class Message(models.Model):
    """Store an internal message exchanged between two registered users."""
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )

    recipient = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="received_messages",
    )

    subject = models.CharField(max_length=150)
    body = models.TextField()
    is_archived = models.BooleanField(default=False)
    is_read  = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)

#Default message ordering
    class Meta:
        ordering = ["-sent_at"]

    def __str__(self):
        return self.subject
