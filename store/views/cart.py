from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View
from store.models.product import Product


class cart(View):
    def get(self,request):
        ids = (list(request.session.get('cart').keys()))
        cart_products = Product.get_products_by_ids(ids)
        print(cart_products)
        return render(request,'cart.html' , {'cart_products':cart_products})