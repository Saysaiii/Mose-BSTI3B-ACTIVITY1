from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, "page/portfolio.html")

def about(request):
    return render(request, 'page/about.html')  # No need to move the file

def project(request):
    return render(request, 'page/project.html')  # No need to move the file

def contact(request):
    return render(request, 'page/contact.html')  # No need to move the file