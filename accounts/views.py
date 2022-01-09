from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render,redirect
from .forms import UserloginForm,UsersignupForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def user_login(request):
    
    if request.method == 'POST':
        form = UserloginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request , username =username, password = password)
            if user:
                login(request, user)
                messages.success(request, ' Logged in succesfully ', 'success')
                return redirect('blog:allArticles')
            else:
                messages.error(request, ' Wrong password... ', 'danger')
        

    else:
        form = UserloginForm()
    return render(request, 'accounts/login.html', {'form': form} )
        

def user_signup(request, backend='django.contrib.auth.backends.ModelBackend'):

    if request.method == 'POST':
        form = UsersignupForm(request.POST)
        if form.is_valid():
            #cd = cleaned data
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'],cd['email'],cd['password1'])
            user.first_name = 'Not Defined yet'
            user.last_name = 'Not Defined yet'
            user.save()
            login(request,user, backend)
            messages.success(request, 'Sign up & Logged in succesfully ', 'success')
            return redirect('blog:allArticles')
        


    else:
        form = UsersignupForm()

    return render(request, 'accounts/signup.html', {'form': form})

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out succesfully', 'success')
    return redirect('blog:allArticles')






    