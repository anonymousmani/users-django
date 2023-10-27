from django.shortcuts import render , HttpResponseRedirect
from django.contrib import messages
#from enroll.form import student_form
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Succefully')
            fm.save()
            return HttpResponseRedirect('/')
    else:
        fm = UserCreationForm()
    return render(request, 'enroll/signup.html', {'form': fm})

def logins(request):
    if request.method == 'POST':
        fm =AuthenticationForm(request=request, data=request.POST)
        print('test2 clear')
        if fm.is_valid():
            print('test3 clear')
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            print('test4 clear')
            if user is not None:
                login(request, user)
                print('test5 clear')
                return HttpResponseRedirect('/profile/')
            else:
                messages.MessageFailure(request, "username and password not matched")
    else:
        fm = AuthenticationForm()
        print('test1 clear')
    return render(request, 'enroll/login.html', {'form': fm})

def profile(request):
    print('test6 clear')
    return render(request, 'enroll/profile.html')
    