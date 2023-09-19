from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    path('welcome/', views.welcome, name = 'welcome'),
    path('forgot_password/', views.forgot_password, name='forgot_password')
]