from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def index_view(requests):
    return HttpResponse('<h1> Home Page </h1>')

def about_view(requests):
    return HttpResponse('<h1> About Page </h1>')

def contact_view(requests):
    return HttpResponse('<h1>Contact Page </h1>')



