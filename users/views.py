from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	return render(request,"pages/index.html")


def custom_login(request,**kwargs):
    if request.user.is_authenticated:
        return redirect("/users/account")
    else:
        return login(request)

@login_required
def account(request):
	return render(request,"registration/showAccInfo.html")

@login_required
def editAccount(request,id):
	if request.method != "POST":
		return render(request,"registration/editAccInfo.html")
	else:
		_first_name = request.POST.get('first_name')
		_last_name = request.POST.get('last_name')
		_email = request.POST.get('email')
		_username = request.POST.get('username')
		_password = request.POST.get('password')

		user = User.objects.get(pk=id)

		user.first_name = _first_name
		user.last_name = _last_name
		user.email = _email
		user.username = _username

		user.save()
		return redirect("/users/account")