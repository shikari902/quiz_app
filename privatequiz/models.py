from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User

class quiz(models.Model):
	name = models.CharField(max_length=255,null=True)
	number_of_questions = models.CharField(max_length=255,null=True)

class question(models.Model):
	quizID = models.CharField(max_length=255,null=True)
	promt = models.CharField(max_length=300,null=True)
	option1 = models.CharField(max_length=300,null=True)
	option2 = models.CharField(max_length=300,null=True)
	option3 = models.CharField(max_length=300,null=True)
	option4 = models.CharField(max_length=300,null=True)
	correct = models.CharField(max_length=300,null=True)