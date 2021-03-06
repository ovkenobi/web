from __future__ import unicode_literals                                         
from django.db import models                                                    
from django.contrib.auth.models import User                                     
                                                                                
class QuestionManager(models.Manager):
    def new(): pass
    def popular(): pass


class Question(models.Model):
    objects = QuestionManager() 
    title = models.CharField(max_length=255)                                    
    text = models.TextField()                                                   
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    rating = models.IntegerField(default = 0) 
    author = models.ForeignKey(User) 
    likes = models.ManyToManyField(User, related_name='question_like_user')


                                                                                
class Answer(models.Model):                                                     
    text = models.TextField() 
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    question = models.ForeignKey(Question) 
    author = models.ForeignKey(User)


