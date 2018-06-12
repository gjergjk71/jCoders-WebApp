from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path("login/", views.custom_login,name="login"),
	path("logout/", auth_views.logout,{'next_page': '/users/login'},name="logout"),
	path("account/", views.account,name="account"),
	path("account/edit/<id>", views.editAccount,name="editAccount"),
	path("account/change_password", views.change_password,name="change_password"),
	path("", views.index, name="index"),
	path("payments/", views.showPayments, name="payments"),
	path("attendances/", views.showAttendances, name="attendances"),
]