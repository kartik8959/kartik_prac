from django.shortcuts import render,redirect
from .models import Institutes,Institute_pic
from .forms import SignUpForm,profile_form
import requests,json,os
from django.contrib.auth.models import User
from django.http import HttpResponse
from .utils import recapcha_test
from cims.settings import BASE_DIR
from django.core.mail import send_mail
from random import randrange
from .email_messages import account_activation_mail
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required



def courses_view(request):
    return render(request,'institutes/courses.html')
    
def pics_upload_view(request,pic_type_id):
        pic=request.FILES.get('file')
        user_id=request.session.get('_auth_user_id')
        institute_pic=Institute_pic(institute_id=user_id,pic_path=pic,pictype_id=pic_type_id)

        institute_pic.save()
        return redirect('/institute/pics/')




def pics_view(request):
    institute_id=request.session.get('_auth_user_id')
    user_id=request.session.get('_auth_user_id')
    interior_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=1)
    exterior_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=2)
    lab_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=3)
    library_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=4)
    classroom_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=5)
    office_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=6)
    parking_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=7)
    sports_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=8)
    facultyroom_pic=Institute_pic.objects.filter(institute_id=user_id,pictype_id=9)
    
    data={
        'interior_pic':interior_pic,
        "exterior_pic":exterior_pic,
        'lab_pic':lab_pic,
        'libraray_pic':library_pic,
        'classroom_pic':classroom_pic,
        'office_pic':office_pic,
        'parking_pic':parking_pic,
        'sports_pic':sports_pic,
        'facultyroom_pic':facultyroom_pic

    }
    return render(request,'institutes/all_pics.html',data)

def dashboard_view(request):
    return render(request,'institutes/dashboard.html')

def profile_pic_upoad_view(request):
    user_id=request.session.get("_auth_user_id")
    try:
        institute=Institutes.objects.get(user_id=user_id)
        old_pic=os.path.join(BASE_DIR,'static/'+institute.logo.url)
        os.remove(old_pic)
    except Institutes.DoesNotExist:
        print("no profile...")
    
    except ValueError:
        pass
    
    logo=request.FILES.get('file')
    print('****************************************')
    print(logo)
    print('****************************************')
    

    institute.logo=logo
    institute.save()
    print("***************************************************")
    request.session['logo']=institute.logo.url
    
    return redirect("/institute/profile")




@login_required(redirect_field_name='login')
def profile_view(request):
    if request.method=="POST":
        pform=profile_form(request.POST)
        if pform.is_valid():
            institute=pform.save(commit=False)
            institute.user_id=request.session.get('_auth_user_id')
            institute.status_id=1
            institute.save()
        return render(request,'institutes/profile.html',{'form':pform})

    else:
        user_id=request.session.get('_auth_user_id')
        try:
            institute=Institutes.objects.get(user_id=user_id)
            form=profile_form(initial={'name':institute.name,'details':institute.details,'address':institute.address,"start_date":institute.start_date,"city":institute.city,'contact':institute.contact})
            return render(request,'institutes/profile.html',{"form":form})
        except Institutes.DoesNotExist:
            print("no profile...")
            return render(request,'institutes/profile.html',{"form":profile_form()})
        


def login_view(request):
    if request.method=="POST":
        print("===================================================================")
        recaptcha_result=recapcha_test(request)
        print('+++++++++++++++++ recaptcha_result ++++++++++++++++++++++++++++++++')
        print(recaptcha_result)
        if recaptcha_result:
            print('**************************************')
            username=request.POST.get('username')
            password=request.POST.get('password')
            print(username,password)
            user=authenticate(request,username=username,password=password)
            print(f'//////////////////////// {user} //////////////////////////////')

            if user is not None:
                login(request,user)
                institute=Institutes.objects.get(user_id=user.id)
                status_id=institute.status_id
                try:
                    request.session['logo']=institute.logo.url
                except ValueError:
                    pass
                if status_id==3:
                    print("-----------------------------------")
                    return redirect('/institute/profile')
                elif status_id==2:
                    print('+++++++++++++++++++++++++')
                    return redirect("home")
                elif status_id==1:
                    print("***********************************")
                    return redirect("dashboard")
            else:
            
                return redirect('/accounts/login')


        else:
            return redirect("/accounts/login")

    else:
         return  redirect("/accounts/login")



def activate_account_view(request):
    username=request.GET.get('username')
    activation_code=request.GET.get('activation_code')
    user=User.objects.get(username=username)

    institute=Institutes.objects.get(user=user,activation_code=activation_code)
    institute.status_id=3
    institute.activation_code=None
    institute.save()
    return redirect("login")

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
                    os.mkdir(institute_folder+"/interior")
                    os.mkdir(institute_folder+"/exterior")
                    os.mkdir(institute_folder+"/lab")
                    os.mkdir(institute_folder+"/library")
                    os.mkdir(institute_folder+"/office")
                    os.mkdir(institute_folder+"/classroom")
                    os.mkdir(institute_folder+"/parking")
                    os.mkdir(institute_folder+"/sportsarea")
                    os.mkdir(institute_folder+"/facultyroom")

                    print("verifying")
                except FileNotFoundError:
                    print("Your folder not exist in folder heirarchy...")

                # subject="activate Your Account"

                # sender="pratapmukesh007@gmail.com"
                # message= account_activation_mail(user.username,activation_code)
                
                # send_mail(subject,"",sender,[user.email],fail_silently=False,html_message=message)

                return redirect("/institute/institute_success/")
            else:
                
                return render(request,'institutes/signup.html',{'form':form})        
        else:
            return redirect('signup')
    else:
        form=SignUpForm()
      
        return render(request,'institutes/signup.html',{'form':form})