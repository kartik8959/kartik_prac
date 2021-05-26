from django.shortcuts import render,redirect
from .models import Institutes
from .forms import SignUpForm
import requests,json,os
from django.contrib.auth.models import User
from django.http import HttpResponse
from .utils import recapcha_test
from cims.settings import BASE_DIR
from django.core.mail import send_mail
from random import randrange
from .email_messages import account_activation_mail

# Create your views here.



def activate_account_view(request):
    username=request.GET.get('username')
    activation_code=request.GET.get('activation_code')
    user=User.objects.get(username=username)

    institute=Institutes.objects.get(user=user,activation_code=activation_code)
    institute.status_id=1
    institute.activation_code=None
    institute.save()
    return HttpResponse("sign in")

def check_username_view(request):
    flag=True
    uname=request.GET.get('username');
    
    try:
        User.objects.get(username=uname)
    except:
        flag=False
    return HttpResponse(flag)
def signup_view(request):
    if request.method=='POST':
        
        recaptcha_test_result=recapcha_test(request)
       
        if recaptcha_test_result:
            form=SignUpForm(request.POST)
            if form.is_valid():
                user=form.save(commit=False)
                user.set_password(user.password)
                user.save()

                contact=request.POST.get('contact_no')

                activation_code=randrange(11111111,99999999)

                institute=Institutes(user=user,contact=contact,activation_code=activation_code)
                institute.save()
                try:
                    institute_folder=os.path.join(BASE_DIR,'static/media/institutes/'+user.username)
                    os.mkdir(institute_folder)
                    print("verifying")
                except FileNotFoundError:
                    print("Your folder not exist in folder heirarchy...")

                subject="activate Your Account"

                sender="pratapmukesh007@gmail.com"
                message= account_activation_mail(user.username,activation_code)
                
                send_mail(subject,"",sender,[user.email],fail_silently=False,html_message=message)

                return redirect("home")
            else:
                
                return render(request,'institutes/signup.html',{'form':form})        
        else:
            return redirect('signup')
    else:
        form=SignUpForm()
      
        return render(request,'institutes/signup.html',{'form':form})