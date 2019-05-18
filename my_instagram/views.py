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

def search(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = Profile.search_by_profile_name(search_term)
        message = f"{search_term}"

        return render(request, 'my_instagram/search.html',{"message":message,"profiles": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my_instagram/search.html',{"message":message})

