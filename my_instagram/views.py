from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from .models import Image, Profile
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required

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

@login_required
def new_post(request):
    current_user=request.user
    if request.method=='POST':
        np_form=NewPostForm(request.POST, request.FILES)
        if np_form.is_valid():
            post=np_form.save(commit=False)
            post.user=current_user
            np_form.save()
            messages.success(request, f'Post Made Successfully!')
        return redirect('my_instagram-home')
    else:
        np_form=NewPostForm(instance=request.user)
        # p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'np_form' : np_form,
    }
    return render(request, 'my_instagram/base.html', context)

