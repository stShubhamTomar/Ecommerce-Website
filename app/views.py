from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
# from django.shortcuts import render
# from django.contrib.auth.views import PasswordChangeView
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
 def get(self, request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobiles = Product.objects.filter(category='M')
  return render(request, 'app/home.html', {'topwears':topwears, 'bottomwears':bottomwears, 'mobiles':mobiles})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
 def get(self, request, pk):
  product = Product.objects.get(pk=pk)
  return render(request, 'app/productdetail.html', {'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')



def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')



def mobile(request, data=None):
 if data == None:
  mobiles = Product.objects.filter(category='M')
 elif data == 'Redmi' or data == 'Samsung':
  mobiles == Product.objects.filter(category='M').filter(brand=data)
 elif data == 'below':
  mobiles = Product.objects.filter(category='M').filter(discount_price_lt=50000)
 elif data == 'above':
  mobiles = Product.objects.filter(category='M').filter(discount_price_gt=50000)
 return render(request, 'app/mobile.html', {'mobiles':mobiles})

def login(request):
 return render(request, 'app/login.html')


class CustomerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'app/customerregistration.html',{'form':form})
 
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   messages.success(request, 'Congratulations!! Registered Successfully') 
   form.save()
   return render(request, 'app/customerregistration.html',{'form':form})
 
def checkout(request):
 return render(request, 'app/checkout.html')

# def logout_log(request):
#  return render(logout(request), return redirect('home'))
 
def logout_view(request):
    logout(request)
    return redirect('login')

# def passwordchangedone(request):
#  return render(request, 'passwordchangedone.html')

class ProfileView(View):
 def get(self, request):
  form = CustomerProfileForm()
  return render(request, 'app/profile.html',{'form':form, 'active':'btn-primary'})
 
  
 def post(self, request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
    usr = request.user
    name = form.cleaned_data['name']
    locality = form.cleaned_data['locality']
    city = form.changed_data['city']
    state = form.changed_data['state']
    zipcode = form.changed_data['zipcode']
    reg = Customer(user=usr, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
    reg.save()
    messages.success(request, 'Congratulations!! Profile Updated Successfully')
    return render(request, 'app/profiel.html', {'form':form, 'active':'btn-primary'})