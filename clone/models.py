import profile
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to = 'images/', null=True)
    bio = models.TextField(blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    
    def __str__(self):
        return self.username
    def profile_save(self):
        self.save()
        
        
    @classmethod
    def search_username(cls,username):
        return User.objects.filter(username=username)

class Image(models.Model):
    name = models.CharField(max_length=30)
    image= models.ImageField(upload_to = 'images/', null=True)
    caption = models.TextField(blank=True)
    post_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, on_delete= models.CASCADE)
    likes = models.ManyToManyField(Profile, related_name="posts")
    
    def __str__(self):
        return self.name
    def save_image(self):
        self.save
    def delete_image(self):
        self.delete()
    def like_count(self):
        return self.likes.count()
    def update_caption(self, new_caption):
        self.caption = new_caption
        self.save()
    
    @classmethod
    def get_profile_image(cls,profile):
        return cls.objects.filter(profile = profile)
    class Meta:
        ordering = ['-post_date']   
        
class Comments(models.Model):
    content = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self) :
        return self.content
    
    def delete_comment(self):
        self.delete()
    
    def save_comment(self):
        self.save()
        
    @classmethod
    def get_image_comments(cls, image):
        return cls.objects.filter(image=image)
    

class Follow(models.Model):
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_followed')
    followers = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='profile_following')
    
    def __str__(self):
        return self.pk