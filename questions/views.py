from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import *
import requests
from pprint import pprint
from .forms import detailForm
import random
from collections import defaultdict
from .models import questions,scores
from django.forms.models import model_to_dict
import time
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.forms import formset_factory


def cleanstring(s):
    s1 = '#039;'
    s2 = '&quot;'
    return s.replace(s1,"'").replace(s2,'"').replace('&','')
    
@login_required(login_url = 'loginPage')
def logoutUser(request):
	logout(request)
	return redirect('loginPage')

@login_required(login_url = 'loginPage')
def leaderboard(request,pk_test):
	if pk_test == 'combined':
		all_scores = scores.objects.all()
	else:
		all_scores = scores.objects.filter(difficulty=pk_test)
	all_score = {}
	arr =[]
	for item in all_scores:
		item = model_to_dict(item)
		arr.append(item)
	j = 0 
	new_arr = []
	var =1
	for item in arr:
		#print(item['userID'])
		username = User.objects.get(id=item['userID'])
		x = model_to_dict(username)
		try:
			f = item['end'].strftime("%H:%M:%S")
		except:
			f = 'Not Found'
		new_arr.append([x['username'] , int(item['marks']) ,int(item['duration']) ,var  ])
		var = var + 1 
	new_arr.sort(key=lambda x:(x[1],-x[2]) , reverse =True)
	var = 1 
	for item in new_arr:
		item[-1] = var
		var = var + 1 

	for item in new_arr:
		all_score[j] = item 
		j = j + 1 
	#all_score = {k:v for k,v in sorted( all_score.items() , key=lambda x:x[1] , reverse=True )}
	return render(request,'leaderboard.html',{'form':all_score})




@login_required(login_url = 'loginPage')
def review(request,pk_test):
	prev_quiz1 = scores.objects.get(quizID = pk_test)
	prev_quiz2 = questions.objects.get(id=pk_test)
	d1 = model_to_dict(prev_quiz1)
	d2 = model_to_dict(prev_quiz2)
	return render(request,'review.html',{'form1':d2 , 'form2':d1})




def registerPage(request):
	form = RegisterForm()
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			person.objects.create(
				user=user,
				name=user.username,
				)
			return redirect('loginPage')
	context = {'form':form}
	return render(request,'register.html',context)

def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			idx = request.user.id
			return redirect('homePage')
		else:
			messages.info(request, 'Username Or Password is wrong')

	context = {}
	return render(request, 'login.html', context)

from collections import defaultdict
@login_required(login_url = 'loginPage')
def homePage(request):
	x = str(request.user.id)
	quizzes = scores.objects.filter(userID=x)
	arr = []	
	for item in quizzes:
		newItem = model_to_dict(item)
		arr.append(newItem)
	previous_scores = dict()
	j = 1
	for item in arr:
		previous_scores[ '/questions/review/'+ str(item['quizID'])] = (item['marks'],item['category'],item['difficulty'],item['end'])


	return render(request, 'homePage.html', {'form': previous_scores})



def cleanedData(questions):
	data = questions['results']
	p = dict()
	for i in range(10):
		p['promt' + str(i+1)] = data[i]['question']
		p['correct'+str(i+1)] = data[i]['correct_answer']
		c = random.randint(1,4)
		p['opt' + str(i+1) + str(c)] = p['correct'+str(i+1)]
		k = 0 
		for j in range(1,5):
			if j!=c:
				p['opt' + str(i+1) + str(j)] = data[i]['incorrect_answers'][k]
				k = k + 1 
	return p

@login_required(login_url = 'loginPage')
def get_questions(request):
	pdict = {'General Knowledge':'9','Books':'10','Flims':'11','Music':'12','Musical and Threaters':'13','Television':'14','Video Games':'15','Board Games':'16','Science and Nature':'17','Computers':'18','Mathematics':'19','Mythology':'20','Sports':'21','Geography':'22','History':'23','Politics':'24','Art':'25','Celebrities':'26','Animals':'27','Vehicles':'28','Comics':'29','Gadgets':'30','Anime and Manga':'31','Cartoon and Animations':'32',}
	ALPHA = {'Medium':'medium','Easy':'easy','Hard':'hard'}
	if request.method == 'POST':
		form = detailForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			response = requests.get('https://opentdb.com/api.php?amount=10&category=' +pdict[str(data['category'])]+'&difficulty=' + ALPHA[str(data['difficulty'])] + '&type=multiple')
			time.sleep(1)
			question = response.json()
			cleaned_dat = cleanedData(question)
			#print(cleaned_data)
			cleaned_data = {}
			cleaned_data['difficulty'] = str(data['difficulty'])
			cleaned_data['category'] =str(data['category'])
			for k,v in cleaned_dat.items():
				cleaned_data[k] = cleanstring(v)
			quiz = questions(**cleaned_data)
			quiz.save()
			quiz_id = str(quiz.id)
			return redirect('/questions/quiz/'+str(quiz_id))   #Find a way to call this function from a different url path
	form = detailForm()
	return render(request, 'generateQuestions.html', {'form': form})
@login_required(login_url = 'loginPage')
def quizInterface(request, pk_test):

	
	f = begin.objects.filter(quizid = pk_test)
	if len(f)>=2:
		return render(request, 'error.html')
	else:

		question = questions.objects.get(id=pk_test)	
		data = model_to_dict(question)
		correct_answer = {}
		for i in range(1,11):
			correct_answer['user_response'+str(i)] = data['correct'+str(i)]
		form = answerForm()


		if request.method == 'POST':
			form = answerForm(request.POST	)
			if form.is_valid():
				time_after = datetime.now()
				#time2 = time_after.strftime("%H:%M:%S")
				#print("Current Time =", time2)
				#duration_of_quiz = int((time_after - time_before).total_seconds())
				#print(duration_of_quiz)
				user_response = form.cleaned_data
				score = 0 
				for k in user_response.keys():
					if user_response[k].lower() == correct_answer[k].lower():
						score = score + 1 

				#print(score)
				userID = str(request.user.id)
				quizID = str(pk_test)

				ALPHA = {'Medium':'Medium','Easy':'Easy','Hard':'Hard'}

				ses = { 'userID' : userID , 'quizID' : quizID , 'marks' : score  , 'category':data['category'] , 'difficulty': ALPHA[data['difficulty'] ]  }
				t = 1 
				for  k in user_response.keys():
					ses['response'+ str(t)] = user_response[k]
					t = t +  1
				obj = scores(**ses)
				obj.save()
				new_obj = begin.objects.get(quizid=pk_test)
				new_dict = model_to_dict(new_obj)
				obj.end=time_after
				obj.begin = new_dict['beg']
				obj.save()
				obj = scores.objects.get(quizID = pk_test)
				stupid  = model_to_dict(obj)
				duration_of_quiz = int((stupid['end'] - stupid['begin']).total_seconds())
				obj.duration = duration_of_quiz
				obj.save()

				return render(request, 'showscore.html',{ 'score':score })
			else:
				pass
		else:

			time_before = datetime.now()
			#time1 = time_before.strftime("%H:%M:%S")
			p = {  'beg':time_before , 'quizid':pk_test  }
			obj = begin(**p)
			obj.save()


		return render(request, 'qa.html',{ 'form1':data , 'form2':form  })


@login_required(login_url = 'loginPage')
def pvtquiz(request):
	
	form = privatequiz()
	if request.method == 'POST':
		form = privatequiz(request.POST	)
		if form.is_valid():
			
			x = pvtquizinfo.objects.all()
			t = []
			for item in x:
				y = model_to_dict(item)
				t.append(y)
			arr = []
			for item in t:
				arr.append( item['name']  )

			print(arr)
			quiz_details = form.cleaned_data
			if quiz_details['name'] in arr:
				return render(request , 'pvtquiz.html' , {'form':form}  )

			obj = pvtquizinfo(**quiz_details)
			obj.save()
			x = model_to_dict(obj)
		return redirect('/questions/pvtquizquestions/' + str(x['id']))      #Direct to the page to add questions

	return render(request , 'pvtquiz.html' , {'form':form}  )

@login_required(login_url = 'loginPage')
def makepvtquestions(request,quizid):
	
	form  = privatequizquestions()
	if request.method == 'POST':
		form = privatequizquestions(request.POST)
		if form.is_valid():
			question_detail = form.cleaned_data
			question_detail['pvtquizID'] = quizid
			obj = privatequestion(**question_detail)
			obj.save()
			return redirect('/questions/homepage'  )

	return render(request , 'pvtquestion.html' , {'form' :form } )
@login_required(login_url = 'loginPage')
def authenticate_load_quiz(request,pk):
	form = roomauth()
	if request.method == 'POST':
		form = roomauth(request.POST	)
		if form.is_valid():
			data = form.cleaned_data 
			try:
				x = pvtquizinfo.objects.get(name = pk )
				y = model_to_dict(x)
				if data['password'] == y['password']:
					try:
						f = pvtbegin.objects.get(quizid = str(y['id']) , userid = str(request.user.id)  )
						return render(request , 'error.html' )
					except:

						time_start = datetime.now()
						ses = { 'beg':time_start , 'quizid':str( y['id'] ) , 'userid' : str(request.user.id)   }
						obj = pvtbegin(**ses)
						obj.save()
						return redirect('/questions/loadpvtquiz/' + str(y['id']) )
				else:
					return render(request , 'wrongpass.html' )
				
			except:
				return redirect('/questions/enterquiz/' + str(pk))

	return render(request , 'enterquiz.html' , {'form' :form } )
@login_required(login_url = 'loginPage')
def allrooms(request):
	x = pvtquizinfo.objects.all()
	arr = []
	d = dict()
	for item in x:
		y = model_to_dict(item)
		arr.append(y)
	i = 1 
	for item in arr:
		if item["publicPassword"] == True:
			link = '/questions/enterquiz/' + str(item['name'])
			link2 = '/questions/pvtleaderboard/' + str(item['id'])
			d[str(item['name'])] = (link,link2,item["password"])
			#print(d)
			i = i  + 1
		else:
			link = '/questions/enterquiz/' + str(item['name'])
			link2 = '/questions/pvtleaderboard/' + str(item['id'])
			d[str(item['name'])] = (link,link2,"******")
			#print(d)
			i = i  + 1

	#print(d)
	return render(request , 'showroom.html' , {'form':d} )



@login_required(login_url = 'loginPage')
def loadpvtquiz(request,pk):
	all_question = privatequestion.objects.get(pvtquizID = pk)
	data = model_to_dict(all_question)
	correct_answer = {}
	for i in range(1,11):
		correct_answer['user_response'+str(i)] = data['correct'+str(i)]
	form = answerForm()
	if request.method == 'POST':
		form = answerForm(request.POST	)
		if form.is_valid():
			x = pvtbegin.objects.get(quizid=str(pk) , userid = str(request.user.id) )
			y = model_to_dict(x)
			time_begin = y['beg']
			time_end = datetime.now()
			user_response = form.cleaned_data
			score = 0 
			for k in user_response.keys():
				if user_response[k].lower() == correct_answer[k].lower():
					score = score + 1 

				#print(score)
			userID = str(request.user.id)
			quizID = str(pk)

				#ALPHA = {'Medium':'Medium','Easy':'Easy','Hard':'Hard'}

			ses = { 'userID' : userID , 'quizID' : quizID , 'marks' : score , 'end' : time_end  }
			t = 1 
			for  k in user_response.keys():
				ses['response'+ str(t)] = user_response[k]
				t = t +  1
			obj = pvtscores(**ses)
			obj.save()
			f = pvtscores.objects.get(userID=userID , quizID = quizID)
			g = model_to_dict(f)
			obj.time = str(int((g['end'] - time_begin).total_seconds()))
			obj.save()


			return render(request, 'showscore.html',{ 'score':score })
		else:
			pass


	
	return render(request , 'loadpvtquiz.html' , {'form1': data , 'form2':form } )



@login_required(login_url = 'loginPage')
def pvtleaderboard(request,pk):
	scores = pvtscores.objects.filter(quizID= pk)
	arr = []
	for item in scores:
		y = model_to_dict(item)
		arr.append(y)
	new_arr = []
	var = 0 
	for item in arr:
		username = User.objects.get(id=item['userID'])
		x = model_to_dict(username)
		if item['time'] != None:
			new_arr.append([x['username'] , int(item['marks']) ,int(item['time']) ,var ])
	var = 1 
	for item in new_arr:
		item[-1] = var
		var = var + 1 
	new_arr.sort(key=lambda x:(x[1],-x[2]) , reverse =True)
	new_arr.sort(key=lambda x:(x[1],-x[2]) , reverse =True)
	all_score = {}
	j = 0 
	for item in new_arr:
		all_score[j] = item 
		j = j + 1 
	#all_score = {k:v for k,v in sorted( all_score.items() , key=lambda x:x[1] , reverse=True )}
	return render(request,'pvtleaderboard.html',{'form':all_score})





"""
Future Plans:
Scrape websited and articles and create automatic questions using ml applications
Option to make the room password visible
Use api's to provide users fun facts and trivia on several topics
"""
