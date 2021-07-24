from django.db import models

from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=164)
    repository_url = models.URLField(max_length=200, blank=True)
    users = models.ManyToManyField(User, related_name='projects')


class ToDo(models.Model):
    DISABLED = 0
    ENABLED = 1
    STATUS_CHOICES = [
        (DISABLED, 'Disabled'),
        (ENABLED, 'Enabled'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField()
    status = models.BooleanField(choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    creator_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')

