from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password 
from django.http import HttpResponse
from store.models.customer import Customer
from django.views import View



class signup(View):
    def get(self,request):
        return render(request,'signup.html')
    
    def post(self,request):
        return self.register(request)

    def register(self,request):
        postdata = request.POST
        first_name = postdata.get('firstname')
        last_name = postdata.get('lastname')
        mobile = postdata.get('mobile')
        email = postdata.get('email')
        password = postdata.get('password')
        print(first_name,last_name,mobile,email,password)
        values={
            'firstname' : first_name,
            'lastname' : last_name,
            'mobile' : mobile,
            'email' : email
        }
            #validation
        customer = Customer(first_name=first_name,last_name=last_name,mobile=mobile,email=email,password=password)
        error_msg = self.validation_of_customer(customer)
            #registration
        if not error_msg:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:
            data = {
            'error':error_msg,
            'values':values
                    }

            return render(request,'signup.html',data)
    
    def validation_of_customer(self,customer):
        error_msg = None
        if (not customer.first_name):
            error_msg = "First Name Required !!"
        elif len(customer.first_name) < 3:
            error_msg = 'First Name must contain minimum 3 characters'
        elif not customer.last_name:
            error_msg = 'Last Name Required'
        elif len(customer.last_name) < 3:
            error_msg = 'Last Name must contain minimum 3 characters '
        elif not customer.mobile:
            error_msg = 'Phone Number required'
        elif len(customer.mobile) < 10:
            error_msg = 'Phone Number must contain 10 numbers'
        elif len(customer.password) < 3:
            error_msg = 'Password must be 3 char long'
        elif len(customer.email) < 5:
            error_msg = 'Email must be 5 char long'
        elif customer.emailcheck():  
            error_msg = 'this email is already in use...'

        return error_msg