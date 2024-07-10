import random
import string
from django.db import models

# Create your models here.

def generate_unique_alphanumeric(length):
    """Generate a unique and random alphanumeric string of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

class Card(models.Model):
    c_id = models.CharField(max_length=2 , unique=True, default=generate_unique_alphanumeric(2))
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    img = models.ImageField(upload_to='static/images', null=True)
