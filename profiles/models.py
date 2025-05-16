from django.contrib.auth.models import User
from django.db import models

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    phone_number=models.CharField(max_length=50, null=True , blank=True)

    def __str__(self):
        return self.user.username if self.user else "بدون کاربر"

