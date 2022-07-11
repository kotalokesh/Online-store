from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name = models.CharField(max_length= 50)
    mobile = models.CharField(max_length= 10)
    email = models.EmailField()
    password = models.CharField(max_length =500)

    def register(self): 
        self.save()
    
    def emailcheck(self):  # for checking if already is email is used or not 
        if Customer.objects.filter(email= self.email):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except : 
            return False
          