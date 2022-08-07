from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import People, Shop
from django.contrib import auth

def index(request):
    if request.session.get('shop_email'):
        return redirect('dashboard')
    else:
        return render(request, 'shop/index.html')

def signup(request):
    if request.session.get('email'):
        return redirect('index')
    else:
        if request.method == 'GET':
            return render(request, 'shop/signup.html')
        elif request.method == 'POST':
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            data = People(full_name=full_name, email=email, password=password)
            data.save()
            request.session['email'] = email
            return redirect('index')


def login(request):
    if request.session.get('email'):
        return redirect('index')
    else:
        if request.method == 'GET':
            return render(request, 'shop/login.html')
        elif request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            data = People.objects.get(email = email)
            
            if password == data.password:
                request.session['email'] = email
                if Shop.objects.filter(email = email).exists():
                    request.session['shop_email'] = email
                else:
                    return redirect('index')
                return redirect('index')
            else:
                return redirect('login')

def shop_registration(request):
    if request.session.get('shop_email'):
        return redirect('dashboard')
    else:
        if request.session.get('email'):
            if request.method == 'GET':
                return render(request, 'shop/shop_registration.html')

            elif request.method == 'POST':
                shop_name = request.POST.get('shop_name')
                shop_email = request.POST.get('shop_email')
                shop_id = "helloljflwoeuroweurweo"

                data = Shop(email=shop_email, shop_name=shop_name, shop_id=shop_id)
                data.save()
                request.session['shop_email'] =  shop_email
                return redirect('dashboard')
        else:
            return redirect('login')

def dashboard(request):
    if request.session.get('shop_email'):
        data = Shop.objects.get(email=request.session.get('shop_email'))
        print(data)
        params = {'data':data}
    else:
        return redirect('login')
    return render(request, 'shop/dashboard.html', params)

def logout(request):
    auth.logout(request)
    return redirect('login')

def profile(request):
    if request.session.get('email'):
        email = request.session.get('shop_email')
        data = Shop.objects.get(email=email)
        params = {'data':data}
        return render(request, 'shop/shop_profile.html', params)
    else:
        return redirect('login')

def settings(request):
    if request.session.get('email'):
        email = request.session.get('shop_email')
        data = Shop.objects.get(email=email)
        params = {'data':data}
        return render(request, 'shop/shop_settings.html', params)
    else:
        return redirect('login')

def add_products(request):
    if request.session.get('email'):
        email = request.session.get('shop_email')
        data = Shop.objects.get(email=email)
        params = {'data':data}
        return render(request, 'shop/add_products.html', params)
    else:
        return redirect('login')

def picture_change(request):
    if request.method == 'POST':
        shop_id = request.POST.get('shop_id')
        files = request.FILES['profile_pic']

        data = Shop.objects.get(shop_id=shop_id)
        data.shop_pic = files
        data.save()

        return redirect('profile')