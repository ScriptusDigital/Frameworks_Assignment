
from django import forms
from .models import Message

#Form for messages
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]


