from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def startfunc(request):
	return HttpResponse("<h1>Home</h1>")
