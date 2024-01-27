from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    if request.user.is_authenticated:
        user_name = request.user.username
        return render(request, 'home.html', {'user_name': user_name})
    else:
        return render(request, 'home.html')
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')#get the names from each label's input name from signup.html for each field-->
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Passwords are different,make sure both passwords are same before submit")
        else:
            my_user=User.objects.create_user(uname,email,pass1)  #for creating a user
            my_user.save()          #for saving the user's data
            return redirect('login')#it will redirect ur page from signup to login once u click on sinup button

        
    return render(request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)#authenticating if thr login creds are correct or not
        if user is not None:#after authentication it will check the user if it has data or not and frther checks if its not empty and have correct data
            login(request,user)#successful login
            return redirect('home')#redirecting to home page after successful login
        else:
            return HttpResponse("Username or password is incorrect !!!")    
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

