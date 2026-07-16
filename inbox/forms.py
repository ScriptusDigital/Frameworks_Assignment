
from django import forms
from .models import Message

#Form for messages
class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]
#Widgets for style
        widgets = {
            "body": forms.Textarea(attrs={"rows": 5, "id": "messagebody"})
        
        }
    def clean_subject(self):
        subject = self.cleaned_data.get("subject", "").strip()

        if len(subject) < 3:
            raise forms.ValidationError(
                "Subject must be at least 3 characters long."
            )
        return subject