from django.urls import path
from . import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', users_views.register, name="register"),  
    path('login/', users_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]