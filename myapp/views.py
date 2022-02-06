
from ast import Try
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Username: ADMIN
# Pass: sahil@123


def home(request):
    return render(request, "home.html")

@login_required(login_url='/signin')
def instructions(request):
    return render(request,"instructions.html")

@login_required(login_url='/signin')
def roomalloc(request):
    return render(request,"roomalloc.html")


def signup(request):
    if request.method == "POST":
        pass1 = request.POST['pass1']
        rollnumber = request.POST['rollnumber']
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST.get('fname')
        lname = request.POST['lname']
        phone = request.POST['phone']

        student_info = User.objects.create_user(rollnumber, pass1)
        student_info.save()
        messages.success(
            request, "Your account has been succesfully created. ")
        return redirect('signin')
    return render(request, "signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['pass1']
        user = authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            login(request, user)
            return redirect("instructions")
        else:
            messages.error(request, "Bad Credintials")
            return redirect('signin')
    else:
        return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect("signin")
