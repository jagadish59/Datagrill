from django.db import models
from ckeditor.fields import RichTextField
from django.urls.base import reverse

# Create your models here.
class News(models.Model):
    Costumer_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=1000, unique=True)
    image = models.ImageField(upload_to='form')
    
    titl = models.CharField(max_length=200)
    description = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Costumer_name

    def get_url(self):
        return reverse("news:news_detail", kwargs={'slug': self.slug})