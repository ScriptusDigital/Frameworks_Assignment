from django.contrib.auth.models import User
from django.test import TestCase, override_settings
from django.urls import reverse

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

@override_settings(
     STORAGES={
          "staticfiles":{
               "BACKEND":"django.contrib.staticfiles.storage.StaticFilesStorage",
          }
     }
)

class InboxViewTests(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(
            username="senderuser",
            password="testpassword123,"
        )

        self.recipient = User.objects.create_user(
            username="recipientuser",
            password="testpassword123,"
        )

        self.outsider = User.objects.create_user(
            username="outsider",
            password="testpassword123,"
        )

        self.message = Message.objects.create(
            sender=self.sender,
            recipient=self.recipient,
            subject="Project Testing Script",
            body="Writing these scripts is a nightmare."
        )

    def test_recipient_can_view_message(self):
        self.client.force_login(self.recipient)
        

        response = self.client.get(
            reverse("message_detail", args=[self.message.pk])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Project Update")
        self.assertTemplateUsed(
            response,
            "inbox/message_detail.html",
        )

    def test_viewing_message_marks_it_as_read(self):
        self.client.force_login(self.recipient)

        self.client.get(
            reverse("message_detail", args=[self.message.pk])
        )

        self.message.refresh_from_db()
        self.assertTrue(self.message.is_read)


    def test_outsider_cannot_view_message(self):
        self.client.force_login(self.outsider)

        response = self.client.get(
            reverse("message_detail", args=[self.message.pk])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("inbox"))


    def test_user_can_send_message(self):
        self.client.force_login(self.sender)

        response = self.client.post(
         reverse("compose_message"),
        {  
            "recipient": self.recipient.pk,
            "subject": "New Test Message",
            "body": "This message was created during testing.",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
             Message.objects.filter(
                sender=self.sender,
                recipient=self.recipient,
                subject="New Test Message",
            ).exists()
        )

