from django.shortcuts import render , redirect
from django.contrib.auth.hashers import  check_password
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View


class login(View):
    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        postdata= request.POST
        email = postdata.get('email')
        password = postdata.get('password')
        customer = Customer.get_customer_by_email(email)
        print(customer)
        error_msg = None
        if customer:
            flag = check_password(password,customer.password)
            if flag :
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('homepage')
            else:
                error_msg= 'email or password is invalid'
                return render(request, 'login.html',{'error': error_msg})

        else:
            error_msg = 'email or password is invalid'
            return render(request, 'login.html',{'error': error_msg})


def logout(request):
    request.session.clear()
    return redirect('login')