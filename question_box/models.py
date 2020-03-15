from django.conf import settings
from django.db import models
from users.models import User


# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(to=User, related_name='questions', on_delete=models.CASCADE, null=True)    
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    # posted_by = 

    def __str__(self):
        return f'{self.title}: {self.body}'

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    answer = models.ForeignKey(to=Question, related_name='answers', on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=500)
    added_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f' Answer: {self.body}, User: {self.user}'