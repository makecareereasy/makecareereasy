
from os import name
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from personality import views

urlpatterns = [
    path('detect',views.capture,name='facedetect'),
    path('home/', login_required (TemplateView.as_view(
        template_name='personality/home.html'
    )), name='personality_home'),
    path('aptitude_test/', login_required(TemplateView.as_view(
        template_name='personality/aptitude_home.html')),
        name='aptitude_home'),
    path('aptitude/test/', views.AptitudeTest.as_view(), name='aptitude_test'),
    path('aptitude/finished/', TemplateView.as_view(
        template_name='personality/aptitude_finished.html'),
        name='aptitude_finished'),
    path('test/', views.PersonalityTest.as_view(), name='personality_test'),
    path('completed/', views.PersonalityCompleted.as_view(), name='personality_completed'),
    path('index/', login_required (TemplateView.as_view(
        template_name='personality/index.html'
    )), name='index'),
     path('team/', views.team, name='team.html'),
    #re_path(r'^admin/',admin.site.urls),
    #url(r'^admin/',admin.site.urls,name='admin'),

]
