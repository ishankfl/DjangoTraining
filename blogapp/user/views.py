from django.shortcuts import render


def rendering_first_template(request):
    context = {'user': 'ishan'}  # Passing user data to template
    return render(request, 'user/home.html', context)  # Rendering the template with context data

def call_extend(request):
    context = {'user': 'ishan'}  # Passing user data to template
    
    return render(request, 'user/extend.html', context)


# navigation bar


# if(certain condition):
#     yo garne
# else:
#     you garne
# class ClassBasedView(View):
#     def get(self,request):
#         return HttpResponse("<h1>Get method called</h1>")

#     def post(self,request):
#         return HttpResponse("<h1>Get method called</h1>")
        