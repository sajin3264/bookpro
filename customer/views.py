from django.shortcuts import render,redirect
from owner.models import Books
from django.views.generic import View
from customer.forms import UserRegistrationForm,PasswordResetForm
from customer.forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.

class CustomerIndex(View):

    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        return render(request,"customer.html",{"books":qs})

class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,"signup.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

        else:
            return render(request,"signup.html",{"form":form})

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user:
                print('Login success')
                login(request,user)
                return redirect("custhome")

            else:
                print('Not a valid user')
                return render(request, "login.html", {"form": form})
def signout(request):
    logout(request)
    return redirect("login")

class PasswordResetView(View):
    def get(self,request):
        form=PasswordResetForm()
        return render(request,'password_reset.html',{'form':form})
    def post(self,request):
        form=PasswordResetForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data.get("oldpassword")
            newpassword=form.cleaned_data.get("newpassword")
            user=authenticate(request,username=request.user,password=oldpassword)
            if user:
                user.set_password(newpassword)
                user.save()
                return redirect("login")
            else:
                return render(request, 'password_reset.html', {'form': form})
        else:
            return render(request,'password_reset.html',{'form':form})
