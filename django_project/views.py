from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message_phone = request.POST['message-phone']
        message = request.POST['message']
        send_mail(
            message_name,                #subject
            message,                     #email body
            message_email,               #from 
            [settings.EMAIL_HOST_USER],  #to
            fail_silently = False)
        subject_user = 'Welcome to Careerchela!'
        message_user = 'Thanks for writing to us, we will get back to you soon!' 
        send_mail(
            subject_user, 
            message_user, 
            settings.EMAIL_HOST_USER, 
            [message_email], 
            fail_silently = False)

        return render(request,'contact.html', {'message_name': message_name})
    else:
        return render(request,'contact.html', {})

def jobs(request):
    return render(request,'jobs.html')
