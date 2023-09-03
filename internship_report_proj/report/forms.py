from django import forms
from .models import WorkSubmission

class WorkSubmissionForm(forms.ModelForm):
    class Meta:
        model = WorkSubmission
        fields = ['intern', 'date', 'worked_on', 'screenshot']