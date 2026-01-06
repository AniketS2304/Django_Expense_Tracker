from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

# Create your views here.
from .models import User

def landing(request):
    return render(request , 'user_auth/index.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        
        user = get_object_or_404(User, email=email)
        hashed_password = user.password
        is_valid = check_password(password, hashed_password)
        print(user)
        if is_valid:
            return redirect('/tracker/')
        else:
            messages.error(request, "Invalid Credentials")
            
    return render(request,'user_auth/login.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Validation
        if not name or not email or not password:
            messages.error(request, 'All fields are required')
            return render(request, 'user_auth/register.html')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'user_auth/register.html')
        
        # Check if user already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
            return render(request, 'user_auth/register.html')
        
        # Create user with hashed password
        user = User.objects.create(
            name=name,
            email=email,
            password=make_password(password)
        )
        
        messages.success(request, 'Account created successfully! Please login.')
        return redirect('login')
    
    return render(request, 'user_auth/register.html')
        
        
        