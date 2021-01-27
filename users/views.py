from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import views as auth_views
from django.utils import translation

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
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