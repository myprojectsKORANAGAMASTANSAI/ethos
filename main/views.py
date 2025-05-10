from django.shortcuts import render
from .models import user_detailes
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
def main(request):
    
    return  render(request,"index.html")

def home(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        service=request.POST.get("service")
        s=user_detailes(name=name,email=email,phone=phone,subject=subject,service=service)
        #print(name,phone,email,subject,service)
        s.save()
        return render(request,"index.html")
def homepage(request):
        return render(request,"home.html")


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:  # Basic verification
                login(request, user)
                info= user_detailes.objects.all()
                return render (request,"user_info.html",{"info":info})
  # Replace with role-based redirect if needed
            else:
                return render(request, "admin_login.html", {"error": "User account is disabled."})
        else:
            return render(request, "admin_login.html", {"error": "Invalid credentials"})

    return render(request, "admin_login.html")

    
    

