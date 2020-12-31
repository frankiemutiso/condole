from django.db import models
from django.utils.text import slugify
# Create your models here.

class Death(models.Model):
    name = models.CharField(max_length=50)
    birth_year = models.IntegerField(null=True)
    death_year = models.IntegerField(null=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Death, self).save(*args, **kwargs)


class Message(models.Model):
    owner = models.ForeignKey(
        Death, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    relationship_with_deceased = models.CharField(max_length=50, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
