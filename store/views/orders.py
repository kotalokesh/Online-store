from django.shortcuts import render , redirect
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View
from store.models.orders import Order



class order(View):
    def get(self,request):
        customer_id = request.session.get('customer_id')
        odrs = Order.get_all_orders_of_customer(customer_id)
        print(odrs)
     
        return render(request,'orders.html',{'orders':odrs})