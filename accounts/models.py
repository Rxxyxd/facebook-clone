from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

class CustomUser(AbstractUser):
    dob = models.DateField(max_length=8, default=datetime.date.today, null=True, blank=True)
    gender_choice = [('M', 'Male'),('F', 'Female')]
    gender = models.CharField(choices=gender_choice, max_length=128, null=True)