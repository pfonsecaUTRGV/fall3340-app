from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.home, name = 'home'),
	#path('login/',views.login_user, name = 'Login'),
	path('logout/',views.logout_user, name = 'logout'),
	path('register/', views.register_user, name = 'register'),
	path('add_bankaccount/', views.add_bankaccount, name = 'add_bankaccount'),

]