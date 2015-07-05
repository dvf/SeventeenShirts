from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


from .forms import UserForm


def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Create a new user object
            User.objects.create_user(
                user_form.cleaned_data['email'],
                user_form.cleaned_data['email'],
                user_form.cleaned_data['password1'],
                first_name=user_form.cleaned_data['first_name'],
                last_name=user_form.cleaned_data['last_name'],
            )

            # Add a success message in the middleware
            messages.success(request, "Registration successful.")

            return redirect('shop:index')
    else:
        user_form = UserForm()

    return render(request, 'accounts/register.html', dict(user_form=user_form))


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user:
            messages.success(request, "Welcome {0}!".format(user.first_name))
        else:
            messages.error(request, "Invalid login credentials.")
            return redirect('shop:index')
    else:
        return redirect('shop:index')