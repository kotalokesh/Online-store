from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views import View
from store.models.orders import Order
from store.models.product import Product
from store.models.customer import Customer


class checkout(View):
    def post(self,request):
        address =request.POST.get('address')
        phone =request.POST.get('phone')
        customer = request.session.get('customer_id')
        email = request.session.get('customer_email')
        cart = request.session.get('cart')
        products = Product.get_products_by_ids(list(cart.keys()))
        print(address,phone,customer,email,products)

        
        for product in products:
            order = Order(customer=Customer(id = customer),
                          product= product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.place_order()
        request.session['cart']={}

        return redirect('cart')
