from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
	user=models.OneToOneField(User, on_delete= models.CASCADE)
	city=models.CharField(max_length=100, default='')
	phone=models.IntegerField(default=0)

class BudgetInfo(models.Model):
    items= models.CharField(max_length=20)
    cost= models.FloatField(blank=False, null=True)
    date_added= models.DateField()
    user= models.ForeignKey(User, on_delete= models.CASCADE)

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)