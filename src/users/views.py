from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db import transaction

from .forms import UserForm, ProfileForm


# Create your views here.
def home(request):
    return render(request, 'users/home.html')


def register(request):
    """view to register user"""

    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            # messages.success(request, f'Votre compte a été créé avec \
            #     succès {username} avec adresse {email}! \
            #         Vous pouvez maintenant vous connecter')
            return redirect('profile')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})


# @login_required
def profile(request):
    user = " "
    context = {
        "user": user
    }
    return render(request, 'users/profile.html', context)


@login_required
@transaction.atomic
def edit_profile(request):

    if request.method == "POST":
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user_form.save()
            return redirect('profile')
        else:
            UserForm()

    else:
        user_form = UserForm(instance=request.user)
        context = {
            'user_form': user_form,
        }
        return render(request, 'users/edit_profile.html', context)