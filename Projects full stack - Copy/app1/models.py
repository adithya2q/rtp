from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class productsinput(models.Model):
    Name=models.CharField(max_length=100)
    Productname=models.CharField(max_length=100)
    Email=models.EmailField()
    PhoneNumber=models.CharField(max_length=10)
    Address=models.TextField()
    PINCODE=models.IntegerField()
    Image=models.ImageField(upload_to="pics")
    Quantity_For_Sale=models.IntegerField()
    Price_per_kg=models.IntegerField()
    Comments= models.TextField()

    def __str__(self):
        return self.Productname



class cartitems(models.Model):
    productname=models.ForeignKey(productsinput,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    Sum_price=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to="pics",default="none")
    seller_name=models.CharField(max_length=100,default="none")

    def __str__(self):
        return self.seller_name


class Orderdetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=False)
    First_name=models.CharField(max_length=100,null=False)
    Last_name=models.CharField(max_length=100,null=False)
    Email=models.EmailField(null=False)
    Phone=models.CharField(max_length=12,null=False)
    Address=models.TextField(null=False)
    City=models.CharField(max_length=50,null=False)
    State=models.CharField(max_length=50,null=False)
    Country=models.CharField(max_length=50,null=False)
    Pincode=models.IntegerField(null=False)
    Total_price=models.IntegerField(null=False)
    Payment_mode=models.CharField(max_length=140,null=False)
    Payment_id=models.CharField(max_length=200,null=True)
    Orderstatuses=(('pending','pending'),('Out for shipping','Out for shipping'),('completed','completed'))
    Status=models.CharField(max_length=140,choices=Orderstatuses,default='pending')
    Message=models.CharField(max_length=540,null=True)
    Tracking_id=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def ___str__(self):
        return f'{self.user}, {self.id}, {self.Tracking_id}'

class Orderitems(models.Model):
    order=models.ForeignKey(Orderdetails,on_delete=models.CASCADE)
    product=models.ForeignKey(productsinput,on_delete=models.CASCADE)
    unit_price_at_purchase=models.IntegerField()
    quantity=models.IntegerField()

    def ___str__(self):
        return f'{self.order.user}, {self.order.id}, {self.order.Tracking_id}'

class Reviews(models.Model):
    Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Email=models.EmailField()
    Review=models.TextField()
    Image=models.ImageField(upload_to='reviewpic',default="Nil")

    def __str__(self):
        return self.Name
