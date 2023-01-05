from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User

class begin(models.Model):
	beg = models.DateTimeField(null=True)
	quizid = models.CharField(max_length=255,null=True)


class person(models.Model):
	user = models.OneToOneField(User,null=True, blank=True,on_delete = models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class scores(models.Model):
	begin = models.DateTimeField(null=True)
	end = models.DateTimeField(null=True)
	duration = models.CharField(max_length=200,null=True)
	quizID = models.CharField(max_length=200)
	userID = models.CharField(max_length=200)
	marks = models.CharField(max_length=200)
	category = models.CharField(max_length=255,null=True)
	difficulty = models.CharField(max_length=255,null=True)
	response1 = models.CharField(max_length=200,null = True)
	response2 = models.CharField(max_length=200,null = True)
	response3 = models.CharField(max_length=200,null = True)
	response4 = models.CharField(max_length=200,null = True)
	response5 = models.CharField(max_length=200,null = True)
	response6 = models.CharField(max_length=200,null = True)
	response7 = models.CharField(max_length=200,null = True)
	response8 = models.CharField(max_length=200,null = True)
	response9 = models.CharField(max_length=200,null = True)
	response10 = models.CharField(max_length=200,null = True)


class questions(models.Model):
	difficulty = models.CharField(max_length=255,null=True)
	category = models.CharField(max_length=255,null=True)
	promt1 = models.CharField(max_length=255)
	correct1 = models.CharField(max_length=255)
	opt11 = models.CharField(max_length=255)
	opt12 = models.CharField(max_length=255)
	opt13 = models.CharField(max_length=255)
	opt14 = models.CharField(max_length=255)

	promt2 = models.CharField(max_length=255)
	correct2 = models.CharField(max_length=255)
	opt21 = models.CharField(max_length=255)
	opt22 = models.CharField(max_length=255)
	opt23 = models.CharField(max_length=255)
	opt24 = models.CharField(max_length=255)

	promt3 = models.CharField(max_length=255)
	correct3 = models.CharField(max_length=255)
	opt31 = models.CharField(max_length=255)
	opt32 = models.CharField(max_length=255)
	opt33 = models.CharField(max_length=255)
	opt34 = models.CharField(max_length=255)

	promt4 = models.CharField(max_length=255)
	correct4 = models.CharField(max_length=255)
	opt41 = models.CharField(max_length=255)
	opt42 = models.CharField(max_length=255)
	opt43 = models.CharField(max_length=255)
	opt44 = models.CharField(max_length=255)

	promt5 = models.CharField(max_length=255)
	correct5 = models.CharField(max_length=255)
	opt51 = models.CharField(max_length=255)
	opt52 = models.CharField(max_length=255)
	opt53 = models.CharField(max_length=255)
	opt54 = models.CharField(max_length=255)

	promt6 = models.CharField(max_length=255)
	correct6 = models.CharField(max_length=255)
	opt61 = models.CharField(max_length=255)
	opt62 = models.CharField(max_length=255)
	opt63 = models.CharField(max_length=255)
	opt64 = models.CharField(max_length=255)

	promt7 = models.CharField(max_length=255)
	correct7 = models.CharField(max_length=255)
	opt71 = models.CharField(max_length=255)
	opt72 = models.CharField(max_length=255)
	opt73 = models.CharField(max_length=255)
	opt74 = models.CharField(max_length=255)

	promt8 = models.CharField(max_length=255)
	correct8 = models.CharField(max_length=255)
	opt81 = models.CharField(max_length=255)
	opt82 = models.CharField(max_length=255)
	opt83 = models.CharField(max_length=255)
	opt84 = models.CharField(max_length=255)

	promt9 = models.CharField(max_length=255)
	correct9 = models.CharField(max_length=255)
	opt91 = models.CharField(max_length=255)
	opt92 = models.CharField(max_length=255)
	opt93 = models.CharField(max_length=255)
	opt94 = models.CharField(max_length=255)

	promt10 = models.CharField(max_length=255)
	correct10 = models.CharField(max_length=255)
	opt101 = models.CharField(max_length=255)
	opt102 = models.CharField(max_length=255)
	opt103 = models.CharField(max_length=255)
	opt104 = models.CharField(max_length=255)


class pvtquizinfo(models.Model):
	name = models.CharField(max_length=255,null=True)
	password = models.CharField(max_length=255,null=True)
	#number_of_questions = models.CharField(max_length=255,null=True)
	publicPassword = models.BooleanField(default=False)

class pvtquestion(models.Model):
	pvtquizID = models.CharField(max_length=255,null=True)
	promt = models.CharField(max_length=300,null=True)
	option1 = models.CharField(max_length=300,null=True)
	option2 = models.CharField(max_length=300,null=True)
	option3 = models.CharField(max_length=300,null=True)
	option4 = models.CharField(max_length=300,null=True)
	correct = models.CharField(max_length=300,null=True)

class pvtquizresponse(models.Model):
	pvtuserID  = models.CharField(max_length=255,null=True)
	pvtquizID =  models.CharField(max_length=255,null=True)
	pvtquestionID =  models.CharField(max_length=255,null=True)
	response =  models.CharField(max_length=255,null=True)
	correct =  models.CharField(max_length=255,null=True)


class privatequestion(models.Model):
	pvtquizID = models.CharField(max_length =255 , null=True)
	promt1 = models.CharField(max_length=255)
	correct1 = models.CharField(max_length=255)
	opt11 = models.CharField(max_length=255)
	opt12 = models.CharField(max_length=255)
	opt13 = models.CharField(max_length=255)
	opt14 = models.CharField(max_length=255)

	promt2 = models.CharField(max_length=255)
	correct2 = models.CharField(max_length=255)
	opt21 = models.CharField(max_length=255)
	opt22 = models.CharField(max_length=255)
	opt23 = models.CharField(max_length=255)
	opt24 = models.CharField(max_length=255)

	promt3 = models.CharField(max_length=255)
	correct3 = models.CharField(max_length=255)
	opt31 = models.CharField(max_length=255)
	opt32 = models.CharField(max_length=255)
	opt33 = models.CharField(max_length=255)
	opt34 = models.CharField(max_length=255)

	promt4 = models.CharField(max_length=255)
	correct4 = models.CharField(max_length=255)
	opt41 = models.CharField(max_length=255)
	opt42 = models.CharField(max_length=255)
	opt43 = models.CharField(max_length=255)
	opt44 = models.CharField(max_length=255)

	promt5 = models.CharField(max_length=255)
	correct5 = models.CharField(max_length=255)
	opt51 = models.CharField(max_length=255)
	opt52 = models.CharField(max_length=255)
	opt53 = models.CharField(max_length=255)
	opt54 = models.CharField(max_length=255)

	promt6 = models.CharField(max_length=255)
	correct6 = models.CharField(max_length=255)
	opt61 = models.CharField(max_length=255)
	opt62 = models.CharField(max_length=255)
	opt63 = models.CharField(max_length=255)
	opt64 = models.CharField(max_length=255)

	promt7 = models.CharField(max_length=255)
	correct7 = models.CharField(max_length=255)
	opt71 = models.CharField(max_length=255)
	opt72 = models.CharField(max_length=255)
	opt73 = models.CharField(max_length=255)
	opt74 = models.CharField(max_length=255)

	promt8 = models.CharField(max_length=255)
	correct8 = models.CharField(max_length=255)
	opt81 = models.CharField(max_length=255)
	opt82 = models.CharField(max_length=255)
	opt83 = models.CharField(max_length=255)
	opt84 = models.CharField(max_length=255)

	promt9 = models.CharField(max_length=255)
	correct9 = models.CharField(max_length=255)
	opt91 = models.CharField(max_length=255)
	opt92 = models.CharField(max_length=255)
	opt93 = models.CharField(max_length=255)
	opt94 = models.CharField(max_length=255)

	promt10 = models.CharField(max_length=255)
	correct10 = models.CharField(max_length=255)
	opt101 = models.CharField(max_length=255)
	opt102 = models.CharField(max_length=255)
	opt103 = models.CharField(max_length=255)
	opt104 = models.CharField(max_length=255)

class pvtscores(models.Model):
	#begin = models.DateTimeField(null=True)
	#end = models.DateTimeField(null=True)
	#duration = models.CharField(max_length=200,null=True)
	quizID = models.CharField(max_length=200)
	userID = models.CharField(max_length=200)
	marks = models.CharField(max_length=200)
	time = models.CharField(max_length =255 ,null=True)
	end = models.DateTimeField(null=True)
	#category = models.CharField(max_length=255,null=True)
	#difficulty = models.CharField(max_length=255,null=True)
	response1 = models.CharField(max_length=200,null = True)
	response2 = models.CharField(max_length=200,null = True)
	response3 = models.CharField(max_length=200,null = True)
	response4 = models.CharField(max_length=200,null = True)
	response5 = models.CharField(max_length=200,null = True)
	response6 = models.CharField(max_length=200,null = True)
	response7 = models.CharField(max_length=200,null = True)
	response8 = models.CharField(max_length=200,null = True)
	response9 = models.CharField(max_length=200,null = True)
	response10 = models.CharField(max_length=200,null = True)


class pvtbegin(models.Model):
	beg = models.DateTimeField(null=True)
	quizid = models.CharField(max_length=255,null=True)
	userid = models.CharField(max_length=255,null=True)

class pvtend(models.Model):
	end = models.DateTimeField(null=True)
	quizid = models.CharField(max_length=255,null=True)
	userid = models.CharField(max_length=255,null=True)
