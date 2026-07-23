from django.contrib.auth.models import User
from django.test import TestCase

from .models import Message

# Create your tests here.
class MessageModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):

        cls.sender = User.objects.create_user(
            username="sender",
            password="testpassword123",
        )

        cls.recipient = User.objects.create_user(
            username="recipient",
            password="testpassword123",
        )

        cls.message = Message.objects.create(
            sender=cls.sender,
            recipient=cls.recipient,
            subject="Project Update",
            body="The project is progressing well.",
        )

    def test_message_content(self):
        message = Message.objects.get(pk=self.message.pk)

        self.assertEqual(message.sender.username, "sender")
        self.assertEqual(message.recipient.username, "recipient")
        self.assertEqual(message.subject, "Project Update")
        self.assertFalse(message.is_read)
        self.assertFalse(message.is_archived)

    def test_message_str_method(self):
        self.assertEqual(str(self.message), "Project Update")
