from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True,related_name="tasks")

    class Meta:
        ordering = ["is_completed", "-date"]

    def __str__(self):
        return f"{self.content[:30]}{'...' if len(self.content) > 30 else ''}"
