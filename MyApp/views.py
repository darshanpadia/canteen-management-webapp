from django.shortcuts import render
# from MyApp.models import User
from MyApp.forms import FormNewUser,FormUserProfileInfo,FormLogin
#
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    form = FormNewUser()
    if request.method == "POST":
        user_form = FormNewUser(request.POST)
        profile_form = FormUserProfileInfo(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = FormNewUser()
        profile_form = FormUserProfileInfo()
                                        # 'form': form
    return render(request, 'users.html', {'user_form':user_form,'profile_form':profile_form})

def user_login(request):
    form = FormLogin()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user = user)
                # return HttpResponse("Account Active")
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("Login Failed")
            print("Username:{} Password:{}".format(username,password))

    else:
        return render(request,'login.html',{})



        # form = FormLogin(request.POST)
        # if form.is_valid():
        #     return index(request)
        # else:
        #     print("ERROR FORM INVALID")

    # return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    # return HttpResponse("Logged Out")
    return HttpResponseRedirect(reverse('index'))
