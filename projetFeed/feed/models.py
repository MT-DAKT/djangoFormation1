from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):
    content = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reponse_to = models.ForeignKey('self', on_delete=models.PROTECT, null=True)