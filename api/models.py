from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=120)
    is_completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.description


