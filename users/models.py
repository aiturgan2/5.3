from django.db import models

# Create your models here.

class User(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_number
    