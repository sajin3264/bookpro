from django.shortcuts import render,redirect
from owner.models import Books
from django.views.generic import View,CreateView,ListView,UpdateView
from customer.forms import UserRegistrationForm,PasswordResetForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from customer.models import Carts
from django.contrib import messages

# Create your views here.

class CustomerIndex(ListView):
    model = Books
    template_name = "customer.html"
    context_object_name = "books"

    # def get(self,request,*args,**kwargs):
    #     qs=Books.objects.all()
    #     return render(request,"customer.html",{"books":qs})

class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
    # def get(self,request,*args,**kwargs):
    #     form=UserRegistrationForm()
    #     return render(request,"signup.html",{"form":form})
    #
    # def post(self,request,*args,**kwargs):
    #     form = UserRegistrationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("login")
    #
    #     else:
    #         return render(request,"signup.html",{"form":form})

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

class PasswordResetView(UpdateView):

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

def add_to_cart(request,id):
    book=Books.objects.get(id=id)
    user=request.user
    cart=Carts(product=book,user=user)
    cart.save()
    messages.success(request,"Item added to Cart")
    return redirect("custhome")

class ViewMyCart(ListView):
    model = Carts
    template_name = "mycart.html"
    context_object_name = "carts"
    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).exclude(status="cancelled").order_by("-date")

def remove_from_cart(request,*args,**kwargs):
    cart=Carts.objects.get(id=kwargs["id"])
    cart.status="cancelled"
    cart.save()
    messages.error(request,"Item is removed")
    return redirect("custhome")