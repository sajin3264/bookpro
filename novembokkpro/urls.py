"""novembokkpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from owner import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("owner/books/add",views.AddBook.as_view(),name="addbook"),
    path("books/all",views.BooklistView.as_view(),name="allbooks"),
    path("books/<int:id>",views.BookDetailView.as_view(),name="booklist"),
    path("books/remove/<int:id>",views.BookDeleteView.as_view(),name="deletebook"),
    path("books/update/<int:id>",views.BookUpdateView.as_view(),name="updatebook"),
    path("customers/",include("customer.urls"))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
