from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import pandas as pd
# Create your views here.
def home(request):
    return render(request,"authentication/index.html")
def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        messages.success(request,"Your account has been successfully created")
        return redirect('signin')

    return render(request,"authentication/signup.html")
def signin(request):
    if request.method =="POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            fname = user.first_name
            df = pd.read_csv('data/NetflixDataset.csv',encoding='ISO-8859-1') 
            movie_list = df['Title'].unique().tolist()
            language_set = set()
            for languages in df['Languages'].dropna().astype(str):
             for language in languages.split(','):
                 language_set.add(language.strip())
            language_list = sorted(language_set)
            return render(request, "authentication/index.html", {'fname': fname, 'movie_list': movie_list,'language_list': language_list})
            
        else:
            messages.error(request,"incorrect password or username")
            return redirect('home')
    return render(request,"authentication/signin.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged out!")
    return redirect('home')