from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from .models import SignupData
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def home(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            return redirect('welcome')

        else:
            error_message = "Wrong username and password"
            print(error_message)

    return render(request, 'Home.html', {'error_message': error_message})

def signup(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username')
        id_number = request.POST.get('id_number')
        cr_number = request.POST.get('cr_number')
        mobile_number = request.POST.get('mobile_number')
        password = request.POST.get('password')
        resident_id_type = request.POST.get('resident_id_type')
        user = None

        if User.objects.filter(username=username).exists():
            error_message = "Username is taken. Please choose a different one"
            print(error_message)

        else:
            user = User.objects.create_user(username, password=password)
            user.save()
            signup_data = SignupData(
                username=username,
                password=password,
                id_number=id_number,
                cr_number=cr_number,
                mobile_number=mobile_number,
                resident_id_type=resident_id_type
            )
            signup_data.save()

        if user is not None:
            return redirect('home')
        else:
            print("The user is not created")


            # user = authenticate(request, username = username, password = password)
            # if user is not None:
            #     login(request, user)
            #     print("User is not none in signup")
            # else:
            #     print("User is none")
            # return redirect('welcome')
    return render(request, 'signup.html', {'error_message': error_message})

def welcome(request):
    return render(request, 'welcome.html')

def forgot_password(request):

    return HttpResponse("Forgot Password Clicked")