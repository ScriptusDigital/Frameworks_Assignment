from datetime import date
from djano.contrib.auth.models import User
from django.test import TestCase 

from .models import Category, Project


class ProjectModelTests(TestCase):

    @class method
    def serUpTestData(cls):
        cls.user = User.objects.create(
            username="testuser",
            password="testpassword123",
        )

    class.category - Category.objects.create(
        name="Web Development",
    )


cls.project = Project.objects.create(
         owner=cls.user,
            name="Test Project",
            description="This is a test project.",
            start_date=date(2026, 7, 1),
            end_date=date(2026, 8, 1),
            stakeholders="Test stakeholder",
            status="planning",
            category=cls.category,

)