from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from .models import Product,OrderPlaced,Customer,Cart
from .forms import CustomerRegistrationForm,CustomerProfileForm
from django.http import HttpResponse, JsonResponse
from django.db.models import Q


def checkout(request):
    user=request.user
    address=Customer.objects.filter(user=user)
    cart=Cart.objects.filter(user=user)
    return render(request,'app/checkout.html',{'address':address,'carts':cart})

def payment_done_view(request):
    cust_id=request.GET.get('custid')
    user=request.user
    carts=Cart.objects.filter(user=user)
    customer=Customer.objects.get(id=cust_id)
    for cart in carts:
        OrderPlaced(user=user,customer=customer,product=cart.product,quantity=cart.quantity).save()
        print("order saved")
        cart.delete()
        print("cart deleted")


    return redirect("orders")

    
def remove_cart_view(request):
    if request.method=="GET":
        print("--------------------------------")
        p_id=request.GET.get('prod_id')
        c=Cart.objects.get(Q(product=p_id) & Q(user=request.user))
        c.delete()
        amount=0.0
        total_amount=0
        shiping_charge=100.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        
         

        for p in cart_product:
            total_amount=(p.quantity*p.product.discount_price)
            amount+=total_amount
        print(cart_product)

        
            

        data={
                "amount":amount,
                "total_amount":amount+shiping_charge

            }            

        return JsonResponse(data)
def plus_cart_view(request):
    if request.method=="GET":
        p_id=request.GET.get('prod_id')
        c=Cart.objects.get(Q(product=p_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount=0.0
        total_amount=0
        shiping_charge=100.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        
        for p in cart_product:
            total_amount=(p.quantity*p.product.discount_price)
            amount+=total_amount
            

            data={
                "quantity":c.quantity,
                "amount":amount,
                "total_amount":amount+shiping_charge

            }            

        return JsonResponse(data)
    

def minus_cart_view(request):
    if request.method=="GET":
        p_id=request.GET.get('prod_id')
        c=Cart.objects.get(Q(product=p_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount=0.0
        total_amount=0
        shiping_charge=100.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        
        for p in cart_product:
            total_amount=(p.quantity*p.product.discount_price)
            amount+=total_amount
            

            data={
                "quantity":c.quantity,
                "amount":amount,
                "total_amount":amount+shiping_charge

            }            

        return JsonResponse(data)


def add_to_cart(request):
    
    user=request.user
    product_id=request.GET.get('prod_id')
    product=Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()

    return redirect("/cart")


def show_cart_view(request):
    if request.user.is_authenticated:
        # print("_______________ ",request.user)

        user=request.user
        cart=Cart.objects.filter(user=user)
        print(cart,"*********")

        amount=0.0
        total_amount=0
        shiping_charge=100.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                total_amount=(p.quantity*p.product.discount_price)
                amount+=total_amount
                total_amount=amount+shiping_charge

            return render(request,'app/addtocart.html',{'carts':cart,'amount':amount,"total_amount":total_amount,"shiping":shiping_charge})

        else:
            return render(request,'app/emptycart.html')







class ProductView(View):
    def get(self,request):
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobile=Product.objects.filter(category='M')
        laptop=Product.objects.filter(category='L')
        return render(request,'app/home.html',{'topwears':topwears,"bottomwears":bottomwears,'mobile':mobile})


class ProductDetailView(View):
    def get(self,request,pk):
        product=Product.objects.get(id=pk)
        return render(request, 'app/productdetail.html',{'product':product})



def buy_now(request):
 return render(request, 'app/buynow.html')

class profile_view(View):
    def get(self,request):
        form=CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})

    def post(self,request):
        form=CustomerProfileForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            user=request.user
            print(user)
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            zipcode=form.cleaned_data['zipcode']
            state=form.cleaned_data['state']
            reg=Customer(user=user,name=name,locality=locality,state=state,city=city,zipcode=zipcode)
            reg.save()
            messages.success(request,"profile uploaded successully.")

            return redirect("/profile/")

        
        return render(request,'app/profile.html',{'form':form,'active':'btn-primary'})


def address(request):
    add=Customer.objects.filter(user=request.user)

    return render(request, 'app/address.html',{'addrs':add,'active':'btn-primary'})

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category="M")
    elif data=="redmi" or data=="samsung":
        mobiles=Product.objects.filter(category="M").filter(brand=data)
    elif data=="above":
        mobiles=Product.objects.filter(category="M").filter(discount_price__gt=10000)
    elif data=="below":
        mobiles=Product.objects.filter(category="M").filter(discount_price__lt=10000)
        

    return render(request, 'app/mobile.html',{'mobiles':mobiles})

def login(request):
 return render(request, 'app/login.html')

class CustomerRegistration_view(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})

    def post(self,request):
        form=CustomerRegistrationForm(request.POST)

        if form.is_valid():
            messages.success(request,"congralatutions !!!! registeed successfull")
            form.save()
        else:
            messages.warning(request,"please fill accurate information")
        return render(request,'app/customerregistration.html',{'form':form})


