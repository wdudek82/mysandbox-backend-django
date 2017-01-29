from django import forms
from .models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'color', 'image', 'about', 'reputation', 'get_comments', 'get_badges', 'date_of_birth']

