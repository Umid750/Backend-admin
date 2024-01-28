from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length = 255)
    def __str__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField(max_length = 255)
    post_content = models.TextField()
    post_image = models.TextField()
    post_category = models.ForeignKey(Category, on_delete = models.CASCADE)
    post_date = models.DateTimeField(auto_now = False)
    def __str__(self):
        return self.post_title
    def get_obsolute_url(self):
        return reverse('post_detail', kwargs = {'pk':self.pk})