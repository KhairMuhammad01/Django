from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponse
from .models import Intern
from django.http import HttpResponseRedirect
from .forms import WorkSubmissionForm
from django.contrib.auth import login, authenticate

# Create your views here.


def home_page(request):
    # return HttpResponse("<b>Hello Interns</b>")
    return render(request, 'home.html') # templates auto search

def work_submission(request):
    print('in work submission function')
    if request.method == 'POST':
        form = WorkSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')  # Redirect after successful submission
    else:
        form = WorkSubmissionForm()
    interns = Intern.objects.all()
    print('interns list ', interns)
    return render(request, 'home.html', {'form': form, 'interns': interns})

def Success(request):
    return render(request, 'success.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        my_user = User.objects.create_user(uname, password=password)
        my_user.save()
        print(uname, password)
        return redirect('login')

    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or password is incorrect")
    return render(request, 'login.html')



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username = username, password = password)
#         if user is not None:
#             login(request, user)
#             return redirect('home')
#         else:
#             error_message = "Invalid Username or Password"
#             return render(request, 'login.html', {'error_message' : error_message})
#     return render(request, 'login.html')
