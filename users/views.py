from django.shortcuts import render
from django.contrib.auth.views import login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from Manage.models import Event,Payment

# Create your views here.

def findStudent(request):
	try:
		student = request.user.student
		hasStudent = True
	except:
		hasStudent = False
	return hasStudent


def custom_login(request,**kwargs):
    if request.user.is_authenticated:
        return redirect("/users/account")
    else:
        return login(request)

@login_required
def showPayments(request):
	try:
		current_user = request.user
		current_user_payments = []
		payments = Payment.objects.all()
		for payment in payments:
			if payment.student == current_user.student:
				current_user_payments.append(payment)
		hasStudent = True
	except:
		hasStudent = False
	context = {"current_user_payments":current_user_payments,"hasStudent":hasStudent}
	return render(request,"pages/payments.html",context)



@login_required
def index(request):
	latestEvent = Event.objects.all().order_by("-opened")[0]
	hasStudent = findStudent(request)
	context = {"latestEvent":latestEvent,"hasStudent":hasStudent}
	return render(request,"pages/index.html",context)


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