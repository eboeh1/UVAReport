from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage
from django.utils import timezone
from django.contrib.auth.models import User


class MyFile(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    )

    uploaded_at = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255, default='',blank=True)
    description = models.TextField()
    file = models.FileField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    admin_notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
