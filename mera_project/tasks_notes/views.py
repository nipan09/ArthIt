from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from tasks_notes.forms import RegisterationForm
from django.contrib.auth import login, logout
from tasks_notes.models import BudgetInfo, UserInfo
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def login_view(request):
	if request.method == 'POST':
		form= AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return HttpResponseRedirect(reverse('app', kwargs={'username':user.username}))
	else: 
		form= AuthenticationForm()
	return render(request, 'registeration/login.html', {'form':form})

def logout_view(request):
	logout(request)
	return redirect('login')

def additem_view(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    BudgetInfo.objects.create(user= request.user,item=name,cost=expense_cost,date_added=expense_date)
    user_qs = UserInfo.objects.filter(name=request.user)
    if user_qs.exists():
    	user_obj = user_qs[0]
    	total = user_obj.total_exp
    	total+= float(expense_cost)
    	user_obj.total_exp = total
    	user_obj.save(update_fields=['total_exp'])
    else:
    	UserInfo.objects.create(name=request.user, total_exp=expense_cost)
    return HttpResponseRedirect(reverse('app', kwargs={'username':request.user}))

def signup_view(request):
	if request.method == 'POST':
		form= RegisterationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return redirect('login')
	else: 
		form=RegisterationForm()
	return render(request, 'tasks_notes/signup.html',{'form':form})

def index_view(request):
	return render(request, 'tasks_notes/index.html')

def app_view(request, username):
	if request.user.is_authenticated:
		budget_qs = UserInfo.objects.filter(name=request.user)
		budget = budget_qs[0].total_exp
		uzer_qs = BudgetInfo.objects.filter(user=request.user).order_by('-date_added')
		return render(request,'tasks_notes/index.html',{'budget':budget,'uzer':uzer_qs[0:5]})
	else:
		return render(request,'tasks_notes/index.html')