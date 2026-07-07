from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    # Allows projects to be organised by category - these are stored as separate model rather than hard-coded so admins can manage viewable categories through the admin panel.
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

# Captured data for each project
class Project(models.Model):

    # Status choices for the project
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('active', 'Active'),
        ('on_hold', 'On Hold'),
        ('completed', 'Completed'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    stakeholders = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projects'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name    