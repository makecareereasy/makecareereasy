from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

from personality.models import PersonalityType

User = settings.AUTH_USER_MODEL

class Applicant(models.Model):
    # user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    user                    = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    personality             = models.ManyToManyField(PersonalityType, blank=True)
    test_score              = models.PositiveIntegerField(default=0)
    taken_apt_test          = models.BooleanField(default=False)
    taken_personality_test  = models.BooleanField(default=False)
    is_employable           = models.CharField(max_length=50, null=True)
    date_joined             = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Applicant.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
