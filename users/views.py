from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import views as auth_views
from django.utils import translation
from django.core.mail import mail_admins, send_mail
from django.utils.translation import gettext

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            msg_title = gettext('Welcome to our site!')
            msg = gettext('Hello, welcome to our website! You can start by adding some recipes and making some plans!')
            send_mail(msg_title, msg, 'noreply@tracker.com', [f'{new_user.email}'])
            mail_admins('New user created!', f'Username: {new_user.username},\nPassword: {new_user.email}')
            messages.success(request, f'Your account has been created, you are able to login now!')
            return redirect('login')
            
    else:
        form = UserRegisterForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


class LoginView(auth_views.LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'

def change_language(request, ln):
    user_language = ln
    translation.activate(user_language)
    request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    return redirect('home')