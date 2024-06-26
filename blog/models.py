from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    email=models.EmailField()
    
    def __str__(self) -> str:
        return self.username
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='profile/',blank=True)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)
    # approve_comments=models.BooleanField(default=False)
    
    def publish(self):
        self.published_date=timezone.now()
        self.save()
        
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.title
    


class Comments(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=50)
    text=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment=True
        self.save()
    
    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
    
        
    def __str__(self) -> str:
        return self.text
    