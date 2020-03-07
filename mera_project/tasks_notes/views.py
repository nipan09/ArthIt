from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from tasks_notes.forms import RegisterationForm
from django.contrib.auth import login, logout
from tasks_notes.models import BudgetInfo

def profile_view(request):
    return render(request, 'tasks_notes/index.html')
'''	user= request.POST['user_name']
	city= request.POST['user_post']
	phone= request.POST['user_phone']'''
	

def login_view(request):
	if request.method == 'POST':
		form= AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return render (request, 'tasks_notes/index.html')
	else: 
		form= AuthenticationForm()
	return render(request, 'registeration/login.html', {'form':form})

def additem_view(request):
    name = request.POST['expense_name']    
    expense_cost = request.POST['cost']  
    expense_date = request.POST['expense_date']
    create=BudgetInfo.objects.create(user= request.user,items=name,cost=expense_cost,date_added=expense_date)
    create.save()
    post= BudgetInfo.objects.all()
    return redirect('app')

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
 
def app_view(request):
	return render(request,'tasks_notes/app.html')