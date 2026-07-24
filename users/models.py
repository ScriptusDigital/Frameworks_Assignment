from django.contrib.auth.models import User

from django.db import models

# User model


# Defined user role choices 

ROLE_CHOICES = [
    ("user", "User"),
    ("manager", "Project Manager"),
    ("admin", "Administrator")

]

# Store user details and app roles for Django user   
# Based on class notes and walkthroughs at https://www.crunchydata.com/blog/extending-djangos-user-model-with-onetoonefield 
# and https://docs.djangoproject.com/en/6.0/topics/db/examples/one_to_one/#
class Profile(models.Model):
    """Store contact details and an application role for a Django user."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")

    def __str__(self):
        return f"{self.user.username} profile"

