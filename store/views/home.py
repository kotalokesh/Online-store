from django.shortcuts import render , redirect
from django.contrib.auth.hashers import make_password , check_password
from django.http import HttpResponse
from store.models.product import Product
from store.models.category import Category
from store.models.customer import Customer
from django.views import View

    


# Create your views here.
class index(View):
    def get(self,request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        categories = Category.get_all_categories()
        category_id = request.GET.get('category')
        if category_id:
            products = Product.get_products_by_category(category_id)
        else:
            products = Product.get_all_products()
        data={}
        data['products'] = products
        data['categories']= categories
        print('you are',request.session.get('customer_email'))
        

        return render(request,'index.html',data)

    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity :
                if remove:
                    if quantity <=1 :
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1
            else:
                cart[product]=1
        else:
            cart = {}
            cart[product]=1
        request.session['cart'] = cart
        print(cart)

        print('product added to cart is',product)
        return redirect('homepage')


def homepage(request):
    return render(request,'homepage.html')