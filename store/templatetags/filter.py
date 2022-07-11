from django import template

register = template.Library()

@register.filter(name='present_in_cart')
def present_in_cart(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return True
    return 
    

@register.filter(name='count')
def count(product,cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='total_priceofproduct')
def total_priceofproduct(product,cart):
    return product.price*count(product,cart)


@register.filter(name='total_price')
def total_price(products,cart):
    sum = 0
    for i in products:
        sum = sum+ total_priceofproduct(i,cart)
    return sum


@register.filter(name='cart_length')
def cart_length(cart):
    try:
        keys = cart.keys()
        if keys:
            value = 0
            for i in cart:
                value = value+cart[i]
            return value
        else:
            return 0
    except Exception as e:
        return 0
    
@register.filter(name='currency')
def currency(price):
    return "₹ "+ str(price)


@register.filter(name='multiply')
def multiply(num1,num2):
    return num1 * num2