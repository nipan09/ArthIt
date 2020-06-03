from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from tasks_notes.forms import RegisterationForm
from django.contrib.auth import login, logout
from tasks_notes.models import BudgetInfo, UserInfo
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

def signup_view(request):
	if request.method == 'POST':
		form= RegisterationForm(request.POST)
		if form.is_valid():
			user=form.save()
			UserInfo.objects.create(name=user, total_exp=0)
			login(request,user)
			return redirect('login')
	else: 
		form=RegisterationForm()
	return render(request, 'tasks_notes/signup.html',{'form':form})

def login_view(request):
	if request.method == 'POST':
		form= AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect('app', username=user.username)
	else: 
		form= AuthenticationForm()
	return render(request, 'registeration/login.html', {'form':form})

def logout_view(request):
	logout(request)
	return redirect('login')

def index_view(request):
	return render(request, 'tasks_notes/index.html')

def additem_view(request):
    name = request.POST['expense_name']
    expense_cost = request.POST['cost']
    expense_date = request.POST['expense_date']
    BudgetInfo.objects.create(user= request.user,item=name,cost=expense_cost,date_added=expense_date)
    user_qs = UserInfo.objects.filter(name=request.user)
    user_obj = user_qs[0]
    total = user_obj.total_exp
    total+= float(expense_cost)
    user_obj.total_exp = total
    user_obj.save(update_fields=['total_exp'])
    return HttpResponseRedirect(reverse('app', kwargs={'username':request.user}))

def app_view(request, username):
	if request.user.is_authenticated:
		budget_qs = UserInfo.objects.filter(name=request.user)
		uzer_qs = BudgetInfo.objects.filter(user=request.user).order_by('-date_added')
		return render(request,'tasks_notes/index.html',{'budget':budget_qs[0],'uzer':uzer_qs[0:5]})
	else:
		return render(request,'tasks_notes/index.html')

def profile_view(request, username):
	if request.method=="GET":
		return render(request,'tasks_notes/app.html')
	if request.method=="POST":
		uzer_qs = UserInfo.objects.filter(name=request.user)
		uzer_obj = uzer_qs[0]
		incm = uzer_obj.income
		incm = request.POST['income']
		uzer_obj.income = incm
		uzer_obj.save(update_fields=['income'])
		return redirect('app',username=request.user)

# Both HttpResponseRedirect(reverse(...)) and redirect(... , ...) works fine