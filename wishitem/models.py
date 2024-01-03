from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through="WishitemProduct")
     
    def __str__(self):
        return str(self.user) 
            

class WishitemProduct(models.Model):
    
    products = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    wishitem = models.ForeignKey(WishItem, null=False, blank=False, on_delete=models.CASCADE)    
