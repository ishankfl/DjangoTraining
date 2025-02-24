
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User
def register(request):
    # request.method === GET, POST
    if request.method == 'GET': #True
        print("Get method")
        data ={'welcome': "Welcome IShan, Register your data"}
        # return HttpResponse("Get method called")
        return render(request, 'user/register.html',data)
    else:
        print(request.POST)
        print("Do register")
        data ={'welcome': "Welcome to LoginPage"}
        user_name = request.POST.get('name')
        user_email =  request.POST.get('email')
        user_password =  request.POST.get('password')
        
        user = User.objects.create(name=user_name, email = user_email, password= user_password)
        
        return redirect('/user/login/')

def login(request):
    if request.method == 'GET':
        data ={'welcome':"Welcome to login page"}
        return render(request, 'user/login.html',data )
    else:
        print(request.POST)
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        try:
            user = User.objects.get(email = user_email, password = user_password)   
            print(user.name) 
            print("User exist")
            request.session['useremail']=user_email
            request.session['username']= user.name
            # return HttpResponse("Login Successed")
            return redirect('/task/crud/')
        except:
            
            print("NOt avaibale")
            return HttpResponse("Login Failed")

        return HttpResponse("Login Successed")

        # return render(request, 'user/login.html',data)

        # return HttpResponse("POST method called")
