from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase 

from .models import Category, Project


class ProjectModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username="testuser",
            password="testpassword123",
    )

        cls.category = Category.objects.create(
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

    def test_project_content(self):
        project = Project.objects.get(pk=self.project.pk)
        self.assertEqual(project.owner.username, "testuser")
        self.assertEqual(project.name, "Test Project")
        self.assertEqual(project.status, "planning")
        self.assertEqual(project.category.name, "Web Development")

    def test_project_str_method(self):
        self.assertEqual(str(self.project), "Test Project")
        self.assertEqual(str(self.category), "Web Development")