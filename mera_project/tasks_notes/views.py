from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def index(request):
	return render(request, 'tasks_notes/index.html')

def login(request):
	return render(request, 'registeration/login.html')

def add_item(request):
    name = request.POST['expense_name']    
    expense_cost = request.POST['cost']  
    expense_date = request.POST['expense_date']
    ExpenseInfo.objects.create(expense_name=name,cost=expense_cost,date_added=expense_date,user_expense=request.user)
    return HttpResponseRedirect('app')


def sign_up(request):
	if request.method=='POST':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return HttpResponseRedirect('app')
	else:
		form= UserCreationForm()
		args= {'form': form}
		return render(request, 'tasks_notes/signup.html', args)