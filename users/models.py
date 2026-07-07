from django.contrib.auth.models import User

from django.db import models

# User model

class Profile(models.Model):
# Based on walkthrough https://www.crunchydata.com/blog/extending-djangos-user-model-with-onetoonefield 
# and https://docs.djangoproject.com/en/6.0/topics/db/examples/one_to_one/#
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, black=True)
    department = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=20)

    def __str_(self):
        return f"{self.user.username} profile"

