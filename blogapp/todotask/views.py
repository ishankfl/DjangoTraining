from django.shortcuts import render, redirect
from django.http import HttpResponse
from user.models import User
from django.core.cache import cache

# Create your views here.
# C=  Create
# R=  Read
# U = Update
# D = Delete
from .models import Task
def crud_task(request):
    if request.method == 'GET':
        if request.session.get('useremail'):
            email_session = (request.session.get('useremail'))
            print("Do get operation")
            # tasks=Task.objects.all()
            user_obj = User.objects.get(email = email_session)
            tasks = Task.objects.filter(user = user_obj).order_by('-created_at')
            data ={'welcome':"Hello User",'data':tasks}
            # to set cahce
            cache.set('tasks', {"hello":"Hello hi"}, timeout=500)  # Cache for 5 minutes

            return render(request, 'todotask/crud_task.html',data)
        else:
            return redirect('/user/login/')
    if request.method == 'POST':
        tasks = cache.get('tasks')
        print("Listed tasskksssss", tasks)

        print("Do post operation")
        task_name = request.POST.get('task_name')
        task_description= request.POST.get('task_description')
        useremail = request.session.get('useremail')
        user_obj = User.objects.get(email = useremail)
        task = Task.objects.create(title=task_name, description = task_description, user = user_obj)
        
        return redirect('/task/crud/')

def update_task(request):
    if (request.method == 'POST'):
        print("Do update")
        task_id = request.POST.get("task_id")        
        task_name_updated = request.POST.get("task_name_updated")        
        task_description_updated = request.POST.get("task_description_updated")
        
        task_update_obj = Task.objects.get(id = task_id)
        task_update_obj.title = task_name_updated
        task_update_obj.description = task_description_updated
        task_update_obj.save()
        
        return redirect ("/task/crud/")
    else:
        return HttpResponse("POST method needed")

def signle_view(request,**kwargs):
    task_id = (kwargs['id'])
    taskobj = Task.objects.get(id = task_id)
    # print(type(kwargs))
    return render(request, 'todotask/single_view.html',{'task':taskobj})
    pass

def delete_view(request, id):
    obj = Task.objects.get(id = id)
    obj.delete()
    return redirect('/task/crud/')  