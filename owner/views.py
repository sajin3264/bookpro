import form as form
from django.shortcuts import render,redirect
from owner.forms import BookForm
from django.views.generic import View
from owner.models import Books

class AddBook(View):
    def get(self,request):
        form=BookForm()
        return render(request,"add_book.html",{"form":form})
    def post(self,request):
        form=BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            # print(form.cleaned_data.get("book_name"))
            # print(form.cleaned_data.get("author"))
            # print(form.cleaned_data.get("price"))
            # print(form.cleaned_data.get("copies"))
            #
            # qs = Books(book_name=form.cleaned_data.get("book_name"), author=form.cleaned_data.get("author"),
            #            amount=form.cleaned_data.get("price"), copies=form.cleaned_data.get("copies"))
            # qs.save()
            print("book created")
            return redirect("allbooks")

            # return render(request,"add_book.html",{"msg":"book created"})
        else:
            return render(request, "add_book.html", {"form": form})

class BooklistView(View):
    def get(self,request):
        qs=Books.objects.all()
        return render(request,'book_list.html',{'books':qs})


class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        # pass
        #kwargs={'id':3}
        qs=Books.objects.get(id=kwargs.get("id"))
        return render(request,"book_details.html",{'book':qs})


class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        qs.delete()
        return redirect("allbooks")

class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.get(id=kwargs.get("id"))
        form=BookForm(instance=qs)
        return render(request,"book_update.html",{'form':form})
    def post(self,request,*args,**kwargs):
        qs = Books.objects.get(id=kwargs.get("id"))
        form=BookForm(request.POST,instance=qs,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("allbooks")
# Create your views here.

# add book
#list all book

# book detail

# edit book

#delete book