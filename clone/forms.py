from django.forms import forms
from .models import Profile, Image, Comments, Follow

class ProfileForm(forms.Form):
    model = Profile
    # exclude ['created', 'account_holder', 'followers', 'following']