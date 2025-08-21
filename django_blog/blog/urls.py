from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #serve built in views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html')),
    #for custom views
    path('register/', views.RegisterView.as_view(), name='register'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
