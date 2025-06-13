from django.db import models

# Create your models here.
class Blogs(models.Model):
    author = models.CharField(max_length=255,default="")
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="blogs/images")
    tags = models.CharField(max_length=200, default="", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.name