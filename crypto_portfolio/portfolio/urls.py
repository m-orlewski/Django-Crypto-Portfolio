from django.urls import path
from . import views
from users import views as users_views
from django.contrib.auth import views as logged_views

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('about/', views.about, name='portfolio-about'),
    path('register/', users_views.register, name = 'portfolio-register'),
    path('profile/', views.profile, name = 'portfolio-profile'),
    path('login/', logged_views.LoginView.as_view(template_name = 'users/login.html'), name = 'portfolio-login'),
    path('logout/', logged_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'portfolio-logout'),
]