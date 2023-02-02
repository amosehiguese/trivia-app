from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.TextField()
    answer = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='questions')
    difficulty = models.PositiveIntegerField()

class Category(models.Model):
    type = models.CharField(max_length=50)