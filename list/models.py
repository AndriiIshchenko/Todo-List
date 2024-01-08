from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)
    TASK_PRIORITY_CHOICE = (
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Normal", "Normal"),
        ("Low", "Low"),
    )
    priority = models.CharField(
        max_length=20,
        choices=TASK_PRIORITY_CHOICE,
        default="Normal",
    )
    tags = models.ManyToManyField(Tag, related_name="tags")
