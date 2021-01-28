from django.urls import path
from . import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', users_views.register, name='register'),  
    path('login/', users_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('change-language/<str:ln>', users_views.change_language, name='change-language'),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='users/reset_password.html'), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'users/password_reset_sent.html'), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'users/password_reset_form.html'), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_done.html'), name ='password_reset_complete'),
]