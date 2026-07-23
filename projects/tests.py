from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase, override_settings

from .forms import ProjectForm
from .models import Category, Project
from django.urls import reverse



class ProjectModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
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

class ProjectFormTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.category = Category.objects.create(
            name="Software",
        )

    def test_project_form_with_valid_data(self):
        form = ProjectForm(
            data={
                "name": "Valid Project",
                "description": "A valid project description.",
                "start_date": "2026-07-01",
                "end_date": "2026-08-01",
                "stakeholders": "Project team",
                "status": "active",
                "category": self.category.pk,
            }
        )

        self.assertTrue(form.is_valid())

    def test_deadline_cannot_be_before_start_date(self):
        form = ProjectForm(
                 data={
                "name": "Invalid Project",
                "description": "Testing invalid dates.",
                "start_date": "2026-08-01",
                "end_date": "2026-07-01",
                "stakeholders": "Project team",
                "status": "planning",
                "category": self.category.pk,
            }
        )

        self.assertFalse(form.is_valid())
        self.assertIn(
            "Deadline must be on or after the start date.",
                form.non_field_errors(),
        )


@override_settings(
     STORAGES={
          "staticfiles":{
               "BACKEND":"django.contrib.staticfiles.storage.StaticFilesStorage",
          }
     }
)


class ProjectViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="projectowner",
            password="testpassword123",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpassword123",
        )

        self.category = Category.objects.create(
            name="Business",
        )

        self.project = Project.objects.create(
            owner=self.user,
            name="View Test Project",
            description="Testing project views.",
            start_date=date(2026, 7, 1),
            end_date=date(2026, 8, 1),
            stakeholders="Test team",
            status="active",
            category=self.category,
        )

    def test_project_list_requires_login(self):
        response = self.client.get(reverse("project_list"))

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

    def test_project_list_view(self):
        self.client.login(
            username="projectowner",
            password="testpassword123",
        )

        response = self.client.get(reverse("project_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Project")
        self.assertTemplateUsed(
            response,
            "projects/project_list.html",
        )

    def test_project_detail_view(self):
        self.client.login(
            username="projectowner",
            password="testpassword123",
        )
        

        response = self.client.get(
            reverse("project_detail", args=[self.project.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Test Project")
        self.assertTemplateUsed(
            response,
            "projects/project_detail.html",
        )

def test_other_user_cannot_view_project(self):
        self.client.login(
        username="otheruser",
        password="testpassword123",
    )

        response = self.client.get(
        reverse("project_detail", args=[self.project.pk])
    )

        self.assertEqual(response.status_code, 404)
     
