from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import views as auth_views

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
