from django.urls import path
from accounts import views
from django.urls import path, reverse_lazy, include


app_name = 'accounts'

urlpatterns = [
    path('registerSeeker/', views.registerSeeker, name='registerSeeker'),
    path('registerCompany/', views.registerCompany, name='registerCompany'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),



]
