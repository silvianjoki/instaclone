import profile
from django.test import TestCase
from models import Profile, Image, Comments, Follow
# Create your tests here.

def test_save_method(self):
    self.james.save_profile()
    Profile = Profile.objects.all()
    self.assertTrue(len(profile) > 0)