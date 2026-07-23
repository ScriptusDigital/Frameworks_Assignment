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
                "username":"SecureTestPassword123!",
                "username":"SecureTestPassword123!",
            }
        )

        self.assertTrue(form.is_valid())


        