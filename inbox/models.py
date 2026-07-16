from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Storing messages sent between users
class Message(models.Model):

    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name="sent_messages",

    )