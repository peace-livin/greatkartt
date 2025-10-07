from django.db import models
from testapp.models import Category
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    discription=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='photos/products')
    stock=models.IntegerField(default=0)
    is_available=models.BooleanField(default=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_data=models.DateTimeField(auto_now_add=True)
    modified_data=models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.product_name