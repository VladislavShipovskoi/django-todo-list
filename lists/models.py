from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    author = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
