from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index_view,name="home"),
    path("sendotp/",views.send_otp_view),
    path('check_otp/',views.check_otp_view),
    path('cities/',views.get_city_view)
    
]