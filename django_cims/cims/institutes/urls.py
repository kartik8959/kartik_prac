from django.urls import path
from institutes import views
from .forms import LoginForm
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('signup/',views.signup_view,name="signup"),
    path('checkusername/',views.check_username_view),
    path('activate_account/',views.activate_account_view),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='institutes/login.html',authentication_form=LoginForm ), name='login'),
]