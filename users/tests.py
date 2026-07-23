from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

from .forms import UserRegisterForm
from .models import Profile


#User reg form test


class UserFormTest(TestCase):

    def test_registration_form_with_valid_data(self):
        form = UserRegisterForm(
            data={
                "username":"newuser",
                "email":"newuser@example.com",
                "password":"SecureTestPassword123!",

            }
        )

        self.assertTrue(form.is_valid())

@override_settings(
     STORAGES={
          "staticfiles":{
               "BACKEND":"django.contrib.staticfiles.storage.StaticFilesStorage",
          }
     }
)

class UserViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="profileuser",
            email="old@example,com",
            password="testpassword123",
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
                "password1":"SecureTestPassword123!",
                "password2":"SecureTestPassword123!",
            }
        )

        self.assertEqual(response.status_code, 302)

        user = User.objects.get(username="registereduser")

        self.assertTrue(
            Profile.objects.filter(user=user).exists()
        )

        self.assertTrue(
            user.check_password("SecureTestPassword123!")
        )

#Profile requires login