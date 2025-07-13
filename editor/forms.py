from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from editor.models import Collaborator


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CollaboratorForm(forms.ModelForm):
    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Select Collaborator")
    role = forms.ChoiceField(choices=Collaborator._meta.get_field('role').choices)

    class Meta:
        model = Collaborator
        fields = ['user', 'role']
