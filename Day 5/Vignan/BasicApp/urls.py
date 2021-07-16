from django.urls import path
from BasicApp import views



urlpatterns = [
	path('demo/',views.demo),
	path('bdemo/',views.bdemo),
	path('register/',views.register),
	path('login/',views.login),
]