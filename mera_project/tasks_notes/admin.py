from django.contrib import admin
from .models import BudgetInfo
from .models import UserProfile

admin.site.register(UserProfile)
admin.site.register(BudgetInfo)

# Register your models here.
