from django.db import models
from django.utils import timezone
# Create your models here.
class Question (models.Model):
    question_text = models.CharField(max_length=200, blank=False, null=False)
    time_pub = models.DateTimeField(default=timezone.datetime.now())
class Choice (models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)