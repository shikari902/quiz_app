from django import forms
from .models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

level = (
    ('Easy','Easy'),
    ('Medium','Medium'),
    ('Hard','Hard'),

    )

topic = (
    ('General Knowledge','General Knowledge'),
    ('Books','Books'),
    ('Flims','Flims'),
    ('Music','Music'),
    ('Musical and Threaters','Musical and Threaters'),
    ('Television','Television'),
    ('Video Games','Video Games'),
    ('Board Games','Board Games'),
    ('Science and Nature','Science and Nature'),
    ('Computers','Computers'),
    ('Mathematics','Mathematics'),
    ('Mythology','Mythology'),
    ('Sports','Sports'),
    ('Geography','Geography'),
    ('History','History'),
    ('Politics','Politics'),
    ('Art','Art'),
    ('Celebrities','Celebrities'),
    ('Animals','Animals'),
    ('Vehicles','Vehicles'),
    ('Comics','Comics'),
    ('Gadgets','Gadgets'),
    ('Anime and Manga','Anime and Manga'),
    ('Cartoon and Animations','Cartoon and Animations')

    )
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class detailForm(forms.Form):
    category = forms.CharField(label='Select Topic', max_length=100 ,widget=forms.Select(choices=topic))
    difficulty  = forms.CharField(label='Select difficulty', max_length=100 ,widget=forms.Select(choices=level))

class answerForm(forms.Form):
    user_response1  = forms.CharField(label='Your Answer for question 1', max_length=100)
    user_response2  = forms.CharField(label='Your Answer for question 2', max_length=100)
    user_response3  = forms.CharField(label='Your Answer for question 3', max_length=100)
    user_response4  = forms.CharField(label='Your Answer for question 4', max_length=100)
    user_response5  = forms.CharField(label='Your Answer for question 5', max_length=100)
    user_response6  = forms.CharField(label='Your Answer for question 6', max_length=100)
    user_response7  = forms.CharField(label='Your Answer for question 7', max_length=100)
    user_response8  = forms.CharField(label='Your Answer for question 8', max_length=100)
    user_response9  = forms.CharField(label='Your Answer for question 9', max_length=100)
    user_response10  = forms.CharField(label='Your Answer for question 10', max_length=100)

class privatequiz(forms.Form):
    name = forms.CharField(label='name' , max_length=255)
    #number_of_questions  = forms.CharField(label='number' , max_length=255)
    password = forms.CharField(label='pass' ,max_length=255,widget=forms.PasswordInput())
    publicPassword = forms.BooleanField(required=False)

class privatequizquestions(forms.Form):
    promt1 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct1 = forms.CharField(max_length=255)
    opt11 = forms.CharField(max_length=255)
    opt12 = forms.CharField(max_length=255)
    opt13 = forms.CharField(max_length=255)
    opt14 = forms.CharField(max_length=255)

    promt2 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct2 = forms.CharField(max_length=255)
    opt21 = forms.CharField(max_length=255)
    opt22 = forms.CharField(max_length=255)
    opt23 = forms.CharField(max_length=255)
    opt24 = forms.CharField(max_length=255)

    promt3 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct3 = forms.CharField(max_length=255)
    opt31 = forms.CharField(max_length=255)
    opt32 = forms.CharField(max_length=255)
    opt33 = forms.CharField(max_length=255)
    opt34 = forms.CharField(max_length=255)

    promt4 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct4 = forms.CharField(max_length=255)
    opt41 = forms.CharField(max_length=255)
    opt42 = forms.CharField(max_length=255)
    opt43 = forms.CharField(max_length=255)
    opt44 = forms.CharField(max_length=255)

    promt5 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct5 = forms.CharField(max_length=255)
    opt51 = forms.CharField(max_length=255)
    opt52 = forms.CharField(max_length=255)
    opt53 = forms.CharField(max_length=255)
    opt54 = forms.CharField(max_length=255)

    promt6 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct6 = forms.CharField(max_length=255)
    opt61 = forms.CharField(max_length=255)
    opt62 = forms.CharField(max_length=255)
    opt63 = forms.CharField(max_length=255)
    opt64 = forms.CharField(max_length=255)

    promt7 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct7 = forms.CharField(max_length=255)
    opt71 = forms.CharField(max_length=255)
    opt72 = forms.CharField(max_length=255)
    opt73 = forms.CharField(max_length=255)
    opt74 = forms.CharField(max_length=255)

    promt8 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct8 = forms.CharField(max_length=255)
    opt81 = forms.CharField(max_length=255)
    opt82 = forms.CharField(max_length=255)
    opt83 = forms.CharField(max_length=255)
    opt84 = forms.CharField(max_length=255)

    promt9 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct9 = forms.CharField(max_length=255)
    opt91 = forms.CharField(max_length=255)
    opt92 = forms.CharField(max_length=255)
    opt93 = forms.CharField(max_length=255)
    opt94 = forms.CharField(max_length=255)

    promt10 = forms.CharField(max_length=255,widget=forms.TextInput(attrs={'style': 'height: 50px;width:1500px'}))
    correct10 = forms.CharField(max_length=255)
    opt101 = forms.CharField(max_length=255)
    opt102 = forms.CharField(max_length=255)
    opt103 = forms.CharField(max_length=255)
    opt104 = forms.CharField(max_length=255)


class roomauth(forms.Form):
    #name = forms.CharField(label='name' , max_length=255)
    password = forms.CharField(label='pass' ,max_length=255,widget=forms.PasswordInput())

class response_form(models.Model):
    user_response = forms.CharField(label='user_response' , max_length=255)

