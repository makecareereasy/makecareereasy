from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import transaction

from .models import Applicant
from django.core.mail import send_mail

# User = settings.AUTH_USER_MODEL
User = get_user_model()
emailid=''
usernameid=''

from allauth.account.forms import SignupForm
from django import forms

class MyCustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        subject_user = "Registration successful"
        message = 'Dear Candidate,\r\r\nWelcome aboard! Your account has been successfully registered. Attempt the aptitude and personality tests for personalised career assessment. \r\r\nMakeCareerEasy is a proud provide free or low-cost career and personality assessments website for charities, non-profits, and schools. Based on validated theories MakeCareerEasy psychometric assessments are a product of hard research and strong alignment to renown psychometric theories and get hired at right place.\r\r\nThanks for trusting us.\r\r\nTeam MakeCareerEasy'
        send_mail(
            subject_user, 
            message,
            settings.EMAIL_HOST_USER, 
            [user.email], 
            fail_silently = False)
        return user 

        

# class ApplicantRegisterForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'first_name', 'last_name')

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         emailid=email
        
#         qs = User.objects.filter(email=email)
#         if qs.exists():
#             raise forms.ValidationError("Email already exists")
#         else:
#             send_mail(
#                 'Make Career Easy Team',
#                 'Welcome onboard! Your account has been registered!!',
#                 'mcareere@gmail.com',
#                 [emailid],
#                 fail_silently= False
#             )
            
#         return email

#     def clean_password2(self):
#         data = self.cleaned_data
#         password1 = data.get('password1')
#         password2 = data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('The passwords you entered are not the same')
#         return password1

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         user.save()
#         usernameid=user
#         applicant = Applicant.objects.create(user=user)
      
#         return user