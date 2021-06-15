from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .utils import send_otp
from .models import City
from django.core.serializers import serialize
import json

def get_city_view(request):
    cities=City.objects.all()
    sr_data=serialize("json",cities)
    # res=json.loads(sr_data)

    print(f"********************** {sr_data} *************************")
    print(f'-------------------------{json.loads(sr_data)} --------------------------------')
    print(f'-------------------------{json.dumps(sr_data)} --------------------------------')
    return HttpResponse(sr_data)

    


def index_view(request):
    return render(request,'index.html')

def send_otp_view(request):
    status=send_otp(request)
    return HttpResponse(status)
    # return HttpResponse("queued")


def check_otp_view(request):
    recived_otp=request.GET.get('otp')
    saved_otp=str(request.session.get('otp'))
    result=recived_otp==saved_otp
    print(recived_otp,saved_otp) 
    print(result)

    return HttpResponse(result)

