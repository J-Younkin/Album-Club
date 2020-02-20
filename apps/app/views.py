from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'app/index.html')

def login_form(request):
    return render(request, "app/sign_in.html")

def create_form(request):
    return render(request, 'app/create_club.html')

    