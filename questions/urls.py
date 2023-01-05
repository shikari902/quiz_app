from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path,include
urlpatterns = [
    path('createQuestions/', views.get_questions,name='createQuestions'),
    #path('quizPage/', views.quiz,name='quiz')
    path('quiz/<str:pk_test>/', views.quizInterface, name="quizInterface"),
    path('register/', views.registerPage, name="registerPage"),
    path('login/', views.loginPage, name="loginPage"),
    path('homepage/', views.homePage, name="homePage"),
    path('review/<str:pk_test>', views.review, name="review"),
    path('leaderboard/<str:pk_test>', views.leaderboard, name="leaderboard"),
    path('logout/', views.logoutUser, name="logout"),
    path('privatequiz/',views.pvtquiz, name="pvtquiz"),
    path('pvtquizquestions/<str:quizid>', views.makepvtquestions, name="makepvtquestions"),
    path('enterquiz/<str:pk>', views.authenticate_load_quiz, name="authenticate_load_quiz"),
    path('loadpvtquiz/<str:pk>', views.loadpvtquiz, name="loadpvtquiz"),
    path('allrooms/', views.allrooms, name="allrooms"),
    path('pvtleaderboard/<str:pk>', views.pvtleaderboard, name="pvtleaderboard"),
    
]
