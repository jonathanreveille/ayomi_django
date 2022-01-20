from django.db import transaction
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from .forms import UserRegisterForm, UserUpdateForm


# Create your views here.
def home(request):
    return render(request, 'users/home.html')

class CustomLoginView(LoginView):
    template_name = "users/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('users:home')


class RegisterPage(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('users:profile')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


@login_required
@transaction.atomic
def profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user_update = User.objects.get(username=request.user.username)
            user_update.email = email
            user_update.save()
            return redirect('users:profile')
    else:
        form = UserUpdateForm(instance=request.user)
        context = {
            'form': form,
        }
        return render(request, 'users/profile.html', context)
    return render(request, 'users/profile.html')
