from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User
# Create your views here.
# C=  Create
# R=  Read
# U = Update
# D = Delete
from .models import Task
def crud_task(request):
    if request.method == 'GET':
        if request.session.get('useremail'):
            print("Do get operation")
            tasks=Task.objects.all()
            data ={'welcome':"Hello User",'data':tasks}

            return render(request, 'todotask/crud_task.html',data)
        else:
            return redirect('/user/login/')
    if request.method == 'POST':
        print("Do post operation")
        task_name = request.POST.get('task_name')
        task_description= request.POST.get('task_description')
        useremail = request.session.get('useremail')
        user_obj = User.objects.get(email = useremail)
        task = Task.objects.create(title=task_name, description = task_description, user = user_obj)
        return redirect('/task/crud/')
        # return HttpResponse("Post method called done")
