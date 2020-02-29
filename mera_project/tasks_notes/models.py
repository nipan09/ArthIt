from django.db import models

class AccountInfo(models.Model):
	username= models.CharField(max_length=20)
	password= models.CharField(max_length=20)

class BudgetInfo(models.Model):
    items= models.CharField(max_length=20)
    cost= models.FloatField(blank=False, null=True)
    date_added= models.DateField(auto_now=True)
    user= models.ForeignKey(AccountInfo, on_delete= models.CASCADE)
    

