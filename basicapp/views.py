from django.shortcuts import render
from basicapp.forms import userinfo,UserProfileInfoform
# Create your views here.
def index(request):
    return render(request,'basicapp/index.html',context={'activeinfo1':'active'})


def registeration(request):
    registered=False
    if request.method=='POST':
        userInfoForm=userinfo(request.POST)
        userProfileForm=UserProfileInfoform(request.POST)
        if userInfoForm.is_valid() and userProfileForm.is_valid():
            userform=userInfoForm.save()
            userform.set_password(userform.password)
            userform.save()
            userProfile=userProfileForm.save(commit=False)
            userProfile.user=userform
            if 'profilepicture' in request.FILES:
                userProfile.profilepicture=request.FILES['profilepicture']
            userProfile.save()
            registered=True
        else:
            print(userInfoForm.errors,userProfileForm.errors)
    userInfoForm=userinfo()
    userProfileForm=UserProfileInfoform()
    content_dict={
        'userform':userInfoForm,
        'userinfoform':userProfileForm,
        'activeinfo3':'active',
        'registerd':registered,
    }
    return render(request,'basicapp/registration.html',context=content_dict)

####for login specific
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect



def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('<h1> Your account is inactive </h1>')
        else:
            print(" Invalid User detected!!! ")
            print("username:",username,"\n",'password: ',password)
            return HttpResponse('<h1> Invalid username and password </h1>')
    else:
        return  render(request,'basicapp/login.html',context={'activeinfo4':'active'})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('basicapp:user_login'))

@login_required
def special(request):
    return HttpResponse('<h1> Hey you selected!!!! </h1>')
