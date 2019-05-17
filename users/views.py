from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} successfully!')
            return redirect('my_instagram-home')
    else:
        form=UserRegisterForm()
    return render (request, 'users/register.html', {'form': form})