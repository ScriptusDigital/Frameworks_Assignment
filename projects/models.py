from django.contrib.auth.models import User
from django.db import models

# Captured data for each project
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    stakeholders = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')

    STAUS_CHOICES = [
        ('planning', 'Planning'),
        ('active', 'Active'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
    ]