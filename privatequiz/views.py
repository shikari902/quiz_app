from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse

def quizdetails(request):
	return render(request, 'start.html')