import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings


class TODOList(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    details = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    list = models.ForeignKey(TODOList, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=100)
    time_created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    time_completed = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.completed and not self.time_completed:
            self.time_completed = timezone.now()
        elif not self.completed and self.time_completed:
            self.time_completed = None
        super().save(*args, **kwargs)
