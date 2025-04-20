from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse

class SignupView(View):
    template_name = 'accounts/signup.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('books:book_list'))
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # Form validation
        errors = {}
        if not username:
            errors['username'] = 'Username is required'
        if not email:
            errors['email'] = 'Email is required'
        if not password:
            errors['password'] = 'Password is required'
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'
        
        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            errors['username'] = 'Username already exists'
        if User.objects.filter(email=email).exists():
            errors['email'] = 'Email already exists'
        
        if errors:
            return render(request, self.template_name, {'errors': errors})
        
        # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect(reverse('books:book_list'))

class LoginView(View):
    template_name = 'accounts/login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse('books:book_list'))
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Form validation
        errors = {}
        if not username:
            errors['username'] = 'Username is required'
        if not password:
            errors['password'] = 'Password is required'
        
        if errors:
            return render(request, self.template_name, {'errors': errors})
        
        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', reverse('books:book_list'))
            return redirect(next_url)
        else:
            errors['auth'] = 'Invalid username or password'
            return render(request, self.template_name, {'errors': errors})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('books:book_list'))