from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from tasks_notes.forms import RegisterationForm
from django.contrib.auth import login, logout
from tasks_notes.models import BudgetInfo


def profile_view(request):
    return render(request, 'tasks_notes/index.html')

def login_view(request):
	if request.method == 'POST':
		form= AuthenticationForm(data=request.POST)
		if form.is_valid():
			user=form.get_user()
			login(request,user)
			return redirect('app')
	else: 
		form= AuthenticationForm()
	return render(request, 'registeration/login.html', {'form':form})

def additem_view(request):
    name = request.POST['expense_name']    
    expense_cost = request.POST['cost']  
    expense_date = request.POST['expense_date']
    BudgetInfo.objects.create(user= request.user,item=name,cost=expense_cost,date_added=expense_date)
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
	bal_qs = [int(obj.cost) for obj in BudgetInfo.objects.filter(user=request.user)]
	budget=0
	for obj in range(len(bal_qs)):
		budget=budget+bal_qs[obj]
	uzer_qs = BudgetInfo.objects.filter(user=request.user).order_by('-date_added')
	return render(request,'tasks_notes/index.html',{'budget':budget,'uzer':uzer_qs[0:5]})

