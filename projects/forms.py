from django import forms
from .models import Project, Category


class ProjectForm(forms.ModelForm):

#Prefill on category field

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True, 
        empty_label="Please select a category",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
# Form inputs

    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'stakeholders', 'status', 'category']

        labels = {
            'end_date': 'Deadline',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control',
            'rows':3                                                                     
                    }),

            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'stakeholders': forms.Textarea(attrs={'class': 'form-control',
            'rows':3                                        
                                                  }),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

#Making sure end date is not before start date

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            raise forms.ValidationError("Deadline must be on or after the start date.")
        
        return cleaned_data