from django.db import models

# Create your models here.
from core.models import BaseModel
class Blog(BaseModel):
    title=models.CharField(max_length=50)
    content=models.TextField(null=True,blank=True)
    content_rich=models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='blog_images', blank=True)

class Comment(BaseModel):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="%(app_label)s_blogs")
    content=models.TextField(null=True,blank=True)
    content_rich=models.TextField(null=True,blank=True)
    