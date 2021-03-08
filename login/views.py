from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import loginform
from django.http import HttpResponse
from register.models import registermodel
from django.contrib.auth import authenticate, login

# Create your views here.
def login(request):
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            username= form.cleaned_data['username']
            password = form.cleaned_data['password']


            if registermodel.objects.filter(modelusername=username).exists():

                 user = registermodel.objects.get(modelusername=username)

                 if user.modelpassword == password:
                     return redirect('display_add')


                 else:

                     return HttpResponse("invalid username/password")
            else:
                form=loginform()
                return render(request,'login/login.html',{'form':form})


    else:
        form=loginform()
        return render(request,'login/login.html',{'form':form})




