from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=30)
    body = RichTextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
