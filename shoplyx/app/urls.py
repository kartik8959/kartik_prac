from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
# from django.contrib.auth.forms import AuthenticationForm
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPassword
urlpatterns = [
    path('', views.ProductView.as_view(),name="home"),
    
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),

    path('cart/',views.show_cart_view,name="show-cart"),
    
    path('buy/', views.buy_now, name='buy-now'),
    
    path('profile/', views.profile_view.as_view(), name='profile'),
    
    path('address/', views.address, name='address'),
    
    path('orders/', views.orders, name='orders'),
    
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name="app/changepassword.html",form_class=MyPasswordChangeForm,success_url="/passwordchangedone/") ,name='changepassword'),
    
    path("passwordchangedone/",auth_views.PasswordChangeDoneView.as_view(template_name="app/passwordchangedone.html"),name="passwordchangedone"),
    
    path('mobile/', views.mobile, name='mobile'),
    
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'),
    
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm ), name='login'),
    
    path("logout/",auth_views.LogoutView.as_view(next_page="login"),name="logout"),
    
    path("password-reset",auth_views.PasswordResetView.as_view(template_name="app/password_reset.html",form_class=MyPasswordResetForm),name="password_rest"),

    path("password-reset/done/done",auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name="app/password-reset-confirm.html",form_class=MySetPassword),name="password_reset_confirm"),
    path("password-reset-complete/",auth_views.PasswordResetCompleteView.as_view(template_name="app/password-reset-complete.html"),name="password_reset_complete"),
    path('registration/', views.CustomerRegistration_view.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    
    path("pluscart/",views.plus_cart_view),
    path("removecart/",views.remove_cart_view),

    path('paymentdone/',views.payment_done_view),

    path("minuscart/",views.minus_cart_view),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

