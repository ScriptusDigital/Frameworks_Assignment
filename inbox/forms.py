
from django import forms
from .models import Message

#Form for messages
class MessageForm(forms.ModelForm):
    recipient = forms.ModelChoiceField(
        queryset=Message._meta.get_field("recipient").remote_field.model.objects.all(),
        empty_label="Choose a recipient",
        widget=forms.Select(attrs={"class": "form-select"})
    )
    class Meta:
        model = Message
        fields = ["recipient", "subject", "body"]

#Widgets for style
        widgets = {
    
             "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter a subject"
                }  
            ),

             "body": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                     "id": "messageBody",
                      "placeholder": "Write your message",
                }  
            ),

        }
    def clean_subject(self):
        subject = self.cleaned_data.get("subject", "").strip()

        if len(subject) < 3:
            raise forms.ValidationError(
                "Subject must be at least 3 characters long."
            )
        return subject