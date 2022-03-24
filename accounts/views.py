from django.shortcuts import render
from django.contrib import messages, auth
from django.http.request import QueryDict
from accounts.models import Account
from django.contrib.auth.decorators import login_required
from django import http
from django.http.response import HttpResponse
import requests
from django.shortcuts import redirect, render

from .forms import RegisterForm

#email imports
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage, message

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email,username=username,password=password)
            user.phone_number = phone_number
            user.save()
            print(username)
            # Sending Email
            current_site = get_current_site(request)
            mail_subject = "Email Verification"
            message = render_to_string('accounts/account_verification_email.html',{
                'user':user,
                'domain':current_site,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject,message,to=[to_email])
            send_email.send()
            #messages.success(request,'Registration is Successful !!! Veriy your email address !')
            return redirect('/account/login/?command=verification&email='+ email)
    else:      
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html',context)

def login(request):
    if request.method == 'POST':
        email = request.POST['email']   
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            messages.success(request, 'Hurray')    
            auth.login(request, user)
            
        else:
            messages.error(request, 'Invalid Email or Password')    
        
    return render(request,'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request,'You are Logged Out !!!')
    return redirect('login')