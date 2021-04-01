from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html')


def lk(request):
    return HttpResponse("Личный Кабинет")


def portfolio(request):
    return render(request, 'main/portfolio-details.html')


def inner(request):
    return render(request, 'main/inner-page.html')


def login(request):
    return render(request, 'account/login.html')


def signup(request):
    return render(request, 'account/signup.html')
