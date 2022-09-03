from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signin/', auth_views.LoginView.as_view(template_name="signin.html")),
    path('signout/', auth_views.LogoutView.as_view(next_page="/")),
    path('customer/', views.customer_page),
    path('courier/', views.courier_page),
]
