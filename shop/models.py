from django.db import models

# Create your models here.
class Product(models.Model):
    Product_id = models.AutoField
    Product_name=models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images" ,default="")
    
    def __str__(self):
        return self.Product_name
    
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)

    
    def __str__(self):
        return self.name
    
class CheckOut(models.Model):
    check_out_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000,default="")
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    zip = models.CharField(max_length=30)
    
    def __str__(self):
        return self.fname +" "+ self.lname

class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    update_desc = models.CharField(max_length=300,default='')
    timestamp = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.update_desc