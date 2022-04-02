
from django import forms
from .models import Profile, Image, Comments, Follow

class ProfileForm(forms.ModelForm):
    model = Profile
    class  Meta:
        model = Profile
        exclude = ('followers', 'following',)

class EditBioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        exclude = ('followed', 'follower',)

class UnfollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        exclude = ('followed', 'follower',)

class UploadImageForm(forms.ModelForm):
    class Meta :
        model = Image
        exclude = ('profile', 'post_date', 'likes',)
