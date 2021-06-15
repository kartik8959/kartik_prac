from django.urls import path
from institutes import views
from .forms import LoginForm
# from django.contrib.auth import views as auth_views

from django.views.generic import TemplateView

urlpatterns=[
    path('signup/',views.signup_view,name="signup"),
    path('checkusername/',views.check_username_view),
    path('activate_account/',views.activate_account_view),
    path("institute_success/",TemplateView.as_view(template_name="institutes/signup_success.html")),
    path('profile/',views.profile_view,name="institute profile"),

    
    
    path('Login/',views.login_view ),

    path('profile_pic_upload/',views.profile_pic_upoad_view),

    path("dashboard/",views.dashboard_view,name="dashboard"),
    path("pics/",views.pics_view,name="all_pics"),
    path("pics_upload/<int:pic_type_id>/",views.pics_upload_view),
    path("courses/",views.courses_view)    
]