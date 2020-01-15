from django.shortcuts import render

def index(request):
	return render(request, 'tasks_notes/index.html')

def login(request):
	return render(request, 'registeration/login.html')

def sign_up(request):
	if request.method=='POST':
		form= UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save()
			login(request,user)
			return HttpResponseRedirect('app')
		else:
			for msg in form.error_messages:
				print(form.error_messages[msg])
	else:
		form= UserCreationForm
		return render(request, 'tasks_notes/signup.html', {'form':form})