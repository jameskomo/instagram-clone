from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, ('my_instagram/base.html'))

def navbar(request):
    return render(request, ('my_instagram/navbar.html'))
