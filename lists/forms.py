from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):

    success = forms.BooleanField(required=False)

    class Meta:
        model = Todo
        fields = ('text', 'priority')
