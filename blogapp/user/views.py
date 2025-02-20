from django.shortcuts import render

# # View function to handle the URL with 'id' and 'category'
# def home(request):
#     context = {'username': 'ishaan'}
#     return render(request, 'home.html', context)
# from django.shortcuts import render

def rendering_first_template(request):
    context = {'user': 'ishan'}  # Passing user data to template
    return render(request, 'user/home.html', context)  # Rendering the template with context data
