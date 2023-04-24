from django.db import models


class Task(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="task")
    header = models.CharField(max_length=255)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    done_or_not = models.BooleanField()

    class Meta:
        ordering = ["-datetime"]
