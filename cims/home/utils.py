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

    print(f"****** {otp} *********")
    request.session['otp']=otp
    print(request.session['otp'])


    account_sid = "ACc10debfe7839ea2af78286d53cd84e9b"

    auth_token  = "bd7c3d7319a16c1c89b96765dd6e082e"

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+91"+contact, 
        from_="+14784199136",
        body="Wellcome to kartik software solutions   "+str(otp))

    print(message.sid)
    print(message.status)

    return message.status
