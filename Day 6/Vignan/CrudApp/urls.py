from django.urls import path
from CrudApp import views


urlpatterns = [
	path('demo/',views.demo),
	path('register/',views.register,name='reg'),
	path('details/',views.details,name='details'),
	path('update/<int:id>',views.update,name='update'),
	path('delete/<int:id>',views.delete,name='delete'),
]