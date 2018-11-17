from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Entry(models.Model):
    # models.Model is part of inheritance that it got from django.db when we imported models from it (at top line)
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)