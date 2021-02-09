from django.db import models

class user_register(models.Model):
      fullname=models.CharField(max_length=70)
      email=models.CharField(max_length=70)
      mobileno=models.CharField(max_length=80,unique=True)
      address=models.CharField(max_length=150)
      username=models.CharField(max_length=30,primary_key=True)
      password=models.CharField(max_length=30)
      status=models.CharField(max_length=20)
class purchase_details(models.Model):
      battery_type=models.CharField(max_length=70)
      serial_no=models.CharField(max_length=70,primary_key=True)
      buyer_name=models.CharField(max_length=80)
      mobno= models.BigIntegerField()
      address=models.CharField(max_length=150)
      purchase_date=models.CharField(max_length=70)
      maintenance_date=models.CharField(max_length=70)
      expiry_date=models.CharField(max_length=70)
      billno=models.IntegerField()
      pincode=models.CharField(max_length=70)
      price=models.BigIntegerField()
      status=models.CharField(max_length=50)

class battery_details(models.Model):
      bimage=models.FileField()
      bname=models.CharField(max_length=70)
      bdesc=models.CharField(max_length=300)
      vtype=models.CharField(max_length=50)
      ftype=models.CharField(max_length=50)
      bvoltage=models.CharField(max_length=30)
      bprice=models.CharField(max_length=50)
      status=models.CharField(max_length=50,default='',null=True)



# Create your models here.
