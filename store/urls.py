"""kotabuy URL Configuration

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
from django.urls import path 
from .views.home import index,homepage
from .views.signup import signup
from .views.login import login, logout
from .views.cart import cart
from .views.checkout import checkout
from .views.orders import order

urlpatterns = [
    path('',index.as_view(), name='homepage'),
    path('signup', signup.as_view()),
    path('login',login.as_view(),name='login'),
    path('logout',logout, name = 'logout'),
    path('cart',cart.as_view(), name = 'cart'),
    path('checkout',checkout.as_view()),
    path('orders',order.as_view()),
    path('homepage',homepage)
]
