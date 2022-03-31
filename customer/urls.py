from django.urls import path
from customer import views

urlpatterns=[
    path("home",views.CustomerIndex.as_view(),name="custhome"),
    path("accounts/register",views.SignUpView.as_view(),name="signup"),
    path("accounts/login",views.LoginView.as_view(),name="login"),
    path("accounts/logout", views.signout,name="logout"),
    path("accounts/password/reset", views.PasswordResetView.as_view(),name="passwordreset"),
    path("carts/items/add/<int:id>",views.add_to_cart,name="addtocart"),
    path("carts/all",views.ViewMyCart.as_view(),name="viewmycart"),
]