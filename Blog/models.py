from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.FileField(upload_to="blog_images/")
    title = models.CharField(max_length=120)
    description = models.TextField()
    hashtag = models.CharField(max_length=100)
    likes = models.IntegerField()
    reposts = models.IntegerField()
