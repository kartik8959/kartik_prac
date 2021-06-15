from twilio.rest import Client
from institutes.models import Institutes
from random import randrange



from .models import City


def prepareCityList():
    cities=City.objects.all()
    cityList=[]
    for city in cities:
        cityList.append((city.id, city.city + " ("+city.state.state+")"))
    
    return cityList


def send_otp(request):
    contact=request.GET.get('contact_no')
    otp=randrange(1111,9999)

   
    request.session['otp']=otp
    print(request.session['otp'])


    account_sid = ""

    auth_token  = ""

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+91"+contact, 
        from_="",
        body="Wellcome to kartik software solutions   "+str(otp))

    print(message.sid)
    print(message.status)

    return message.status
