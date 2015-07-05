from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User


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
