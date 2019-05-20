from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!. Login')
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render (request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'You Account has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form' : u_form,
        'p_form': u_form

    }
    return render(request, 'users/profile.html', context)

def search(request):

    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profiles = user.search_by_username(search_term)
        message = f"{search_term}"

        return render(request, 'my_instagram/search.html',{"message":message,"profiles": searched_profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my_instagram/search.html',{"message":message})

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!. Login')
            form.save()
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render (request, 'users/register.html', {'form': form})

