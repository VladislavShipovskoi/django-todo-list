from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Todo(models.Model):

    PRIORITY = (
        ('1', 'Low'),
        ('2', 'Normal'),
        ('3', 'High'),
    )
    text = models.TextField(max_length=50)
    author = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY,default='2',max_length=6)
    created_date = models.DateTimeField(
        default=timezone.now)
    completed_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.created_date = timezone.now()
        self.save()