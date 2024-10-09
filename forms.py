from django import forms
from .models import MyModel # type: ignore

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = [
            'category',
            'remarks',
            'start_date',
            'end_date',
            'executive_name',
            'user_box',
            'entry_name',
        ]
        
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'remarks': forms.Textarea(attrs={'rows': 4}),
        }
