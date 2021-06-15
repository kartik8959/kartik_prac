import requests,json
def recapcha_test(request):
    grecapresp=request.POST.get('g-recaptcha-response')
    secretkey=''
    url='https://www.google.com/recaptcha/api/siteverify'
    postparams={'secret':secretkey,'response':grecapresp}
    resp=requests.post(url,data=postparams)

    rest_dict=json.loads(resp.text)
    
    return rest_dict
