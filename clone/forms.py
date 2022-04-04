
from django import forms
from .models import Profile, Image, Comments

class ProfileForm(forms.ModelForm):
    model = Profile
    class  Meta:
        model = Profile
        exclude = ['followers', 'following']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['image']

class UploadImageForm(forms.ModelForm):
    class Meta :
        model = Image
        exclude = ['profile', 'post_date', 'likes']
