from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    Price = models.IntegerField(default=0)
    subcategory = models.CharField(max_length=50, default="")
    product_desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=60, default="")
    phone = models.CharField(max_length=20, default="")
    desc = models.CharField(max_length=500, default="")



    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id= models.AutoField(primary_key=True)
    items_json= models.CharField(max_length=5000)
    name=models.CharField(max_length=90)
    amount=models.IntegerField(default=0)
    email=models.CharField(max_length=30)
    phone = models.CharField(max_length=20, default="")
    address=models.CharField(max_length=150, default="")
    city=models.CharField(max_length=150, default="")
    state=models.CharField(max_length=160, default="")
    zip_code=models.CharField(max_length=12, default="")