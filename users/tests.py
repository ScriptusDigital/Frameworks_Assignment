from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from .forms import UserRegisterForm
from .models import Profile


#User reg form test


class UserFormTest(TestCase):
    """Tests for the user registration form."""
    def test_registration_form_with_valid_data(self):
        form = UserRegisterForm(
            data={
                "username":"newuser",
                "email":"newuser@example.com",
                "password1": "A7!qZ9@kLm2#Vp8$",
                "password2": "A7!qZ9@kLm2#Vp8$",

            }
        )

        self.assertTrue(form.is_valid(), form.errors)

@override_settings(
     STORAGES={
          "staticfiles":{
               "BACKEND":"django.contrib.staticfiles.storage.StaticFilesStorage",
          }
     }
)

class UserViewTests(TestCase):
    """Tests for registration, profiles and login protection."""
    def setUp(self):
        self.user = User.objects.create_user(
            username="profileuser",
            email="old@example.com",
            password="A7!qZ9@kLm2#Vp8$",
        )

        self.profile = Profile.objects.create(
            user=self.user,
        )

#Reg creates a user and profile

    def test_registration_creates_user_and_profile(self):
        response = self.client.post(
            reverse("register"),
            {
                "username":"newuser",
                "email":"newuser@example.com",
                "password1":"A7!qZ9@kLm2#Vp8$!",
                "password2":"A7!qZ9@kLm2#Vp8$!",
            }
        )

        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username="newuser")

        self.assertTrue(
            Profile.objects.filter(user=user).exists()
        )

        self.assertTrue(
            user.check_password("A7!qZ9@kLm2#Vp8$!")
        )

#Profile requires login

    def test_profile_requires_login(self):
        response = self.client.get(reverse("profile"))
         

        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("login"), response.url)

#User update profile info
    def test_user_can_update_profile(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("profile"),
            {
                "first_name": "Richard",
                "last_name": "Davies",
                "email": "richard@example.com",
                "phone": "0123456789",
                "department": "Development",
            },
        )

        self.assertEqual(response.status_code, 302)


        self.user.refresh_from_db()
        self.profile.refresh_from_db()

        self.assertEqual(self.user.first_name, "Richard")
        self.assertEqual(self.user.last_name, "Davies")
        self.assertEqual(self.user.email, "richard@example.com",)
        self.assertEqual(self.profile.department, "Development",)