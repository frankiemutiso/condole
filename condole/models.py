from django.db import models

# Create your models here.
from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    relationship_with_deceased = models.CharField(max_length=50, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
