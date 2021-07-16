from django.urls import path
from CrudApp import views


urlpatterns = [
	path('demo/',views.demo),
]