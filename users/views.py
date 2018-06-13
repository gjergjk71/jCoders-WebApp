from django.shortcuts import render
from django.contrib.auth.views import login
from django.contrib.auth import authenticate, update_session_auth_hash
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from Manage.models import Event,Payment,Attendance
from django.contrib import messages

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
		return redirect("/users/")
	elif request.method == "POST":            
		username=request.POST.get("username")
		password = request.POST.get("password")                     
		user = authenticate(request, username=username, password=password)
		if user is not None:
			return login(request)
		else:
			return render(request,"registration/login.html",{'invalid': True })
	elif request.method == "GET":
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
def showAttendances(request):
	try:
		current_user = request.user
		current_user_attendances = []
		attendances = Attendance.objects.all()
		for attendance in attendances:
			if attendance.student == current_user.student:
				current_user_attendances.append(attendance)
		hasStudent = True
	except:
		hasStudent = False
	context = {"current_user_attendances":current_user_attendances,"hasStudent":hasStudent}
	return render(request,"pages/attendance.html",context)

@login_required
def index(request):
	latestEvent = Event.objects.all().order_by("-opened")[0]
	latestPayment = Payment.objects.all().order_by("-id")[0]
	hasStudent = findStudent(request)
	if hasStudent:
		if current_user_payments:
			context = {"latestEvent":latestEvent,"latestPayment":current_user_payments[-1],"hasStudent":hasStudent}
		else:
			context = {"latestEvent":latestEvent,"hasStudent":hasStudent}
	else:
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
		#Removed a line here -------

		user = User.objects.get(pk=id)

		user.first_name = _first_name
		user.last_name = _last_name
		user.email = _email
		user.username = _username

		user.save()
		return redirect("/users/account")


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return render(request,"registration/change_password.html",{'form': form,"successful":True})
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })