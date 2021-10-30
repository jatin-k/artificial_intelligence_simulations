from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'chatbot/home.html', {'title':'chatbot'})