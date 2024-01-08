from django.shortcuts import render
from django.http import HttpResponse
from .models import countModel

# Create your views here.
def startfunc(request):
	return HttpResponse("<h1>Start</h1>");
