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
    try:
        balance = [int(obj.cost) for obj in BudgetInfo.objects.filter(user=request.user)]
        BudgetInfo.objects.filter(user=request.user).update(cost=int(balance[0])+int(expense_cost))   
    except Exception as e:
        create = BudgetInfo.objects.create(user= request.user,items=name,cost=expense_cost,date_added=expense_date)
        create.save()
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
	budget_qs=BudgetInfo.objects.filter(user=request.user)
	budget=budget_qs[0].cost
	return render(request,'tasks_notes/index.html',{'budget':budget})
