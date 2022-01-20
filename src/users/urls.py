from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views
from .views import CustomLoginView, RegisterPage


app_name = "users"


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/',LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('register', RegisterPage.as_view(), name="register"),
    path('profile/', views.profile, name="profile")
]
