# blog/models.py

from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    # Add this line for the image field
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title

    # Optional: Add a method to get the image URL easily in templates
    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return None # Or a default image URL