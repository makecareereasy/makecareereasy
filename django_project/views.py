from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
class Home(TemplateView):
    template_name = 'home.html'
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def courses(request):
    return render(request,'courses.html')
def teacher(request):
    return render(request,'teacher.html')
def test(request):
    return render(request,'test.html')
def contact(request):
    return render(request,'contact.html')
def jobs(request):
    return render(request,'jobs.html')
