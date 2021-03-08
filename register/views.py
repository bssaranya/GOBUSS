from django.shortcuts import render, redirect
from register.models import registermodel
from .forms import registerform
from django.contrib import messages
from django.core.mail.message import EmailMessage
from django.contrib.auth.models import User
from login.forms import loginform


# Create your views here.


def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phno = form.cleaned_data['phno']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            confirmpassword = form.cleaned_data['confirmpassword']
            if confirmpassword == password:
                reg = registermodel()
                reg.modelname = name
                reg.modelphno = phno
                reg.modelemail = email
                reg.modelusername = username
                reg.modelpassword = password
                reg.modelconfirmpassword = confirmpassword
                if registermodel.objects.filter(modelusername=username).exists():
                    messages.warning(request, "username exist ")
                    return redirect('register')

                else:
                    reg.save()

            else:
                print("password mismatch")
                return redirect('register')

        return redirect('login')
    else:
        form = registerform()
        return render(request, 'register/register.html', {'form': form})


