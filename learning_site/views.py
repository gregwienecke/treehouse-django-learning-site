from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
	return render(request, 'home.html')

def test(request):
	return render(request, 'test.html')