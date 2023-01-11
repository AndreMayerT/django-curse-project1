from django.http import HttpResponse

# from django.shortcuts import render

# Create your views here.


def home(req):
    return HttpResponse('Home')


def contact(req):
    return HttpResponse('Contact')


def about(req):
    return HttpResponse('About')
