from django.db import models
from datetime import datetime

class user_detailes(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=1000)
    service = models.CharField(max_length=225)
    created_at = models.DateTimeField(default=datetime.now)  # Manually set default value
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
