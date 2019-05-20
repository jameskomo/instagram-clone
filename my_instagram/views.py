from django.shortcuts import render
from django.http import Http404
from .models import Image, Profile

# Create your views here.
def home(request):
    context = {
        'images':Image.objects.all(),
        'profiles': Profile.objects.all()
    }
    return render(request, ('my_instagram/base.html'), context)

def profile(request):
    context = {
        'images':Image.objects.all()
    }
    return render(request, ('my_instagram/profile.html'), context)



