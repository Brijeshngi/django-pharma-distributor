from django.db import models

# Create your models here.

class product(models.Model):

    PRODUCT_TYPE = (
        ('Patent','Patent'),
        ('Generic','Generic')
    )

    product_name =  models.CharField(max_length=100)
    brand = models.ForeignKey('brand', on_delete=models.SET_NULL , null= True)
    product_Quality_type = models.CharField(max_length=100, choices=PRODUCT_TYPE)
    product_category = models.ForeignKey('product_category', on_delete=models.SET_NULL, null = True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    deal = models.CharField(max_length=100)
    discount = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='product_image', blank=True, null=True)
    batch_number = models.CharField(max_length=100, blank=True, null=True)
    Stock_quantity = models.DecimalField(max_digits=1000, decimal_places=2, blank=True, null=True)
    Packing_Value = models.CharField(max_length=100,blank=True, null=True)
    MFG_Date = models.CharField(max_length=20, blank=True, null=True)
    EXP_Date = models.CharField(max_length=20, blank=True, null=True)
    Date_Of_Purchase_in_Stock = models.CharField(max_length=100, blank=True, null=True)
    Date_Of_Billing_From_Stock = models.CharField(max_length=100, blank=True, null=True)
    Supplier_detail = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name

class product_category(models.Model):
    productCategory = models.CharField(max_length=100)


    def __str__(self):
        return self.productCategory


class brand(models.Model):


    brand_name = models.CharField(max_length=100)
    brand_logo = models.ImageField(upload_to='brand_logo', blank=True, null=True )


    def __str__(self):
        return self.brand_name

class customer(models.Model):

    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Firm_name = models.CharField(max_length=100)
    Drug_license_number = models.CharField(max_length=100)
    GSTIN = models.CharField(max_length=15)
    Address = models.CharField(max_length=100)

    def __str__(self):
        return self.FirstName




class UserLogin(models.Model):

    EmailId = models.EmailField(max_length=100)
    password1 =  models.CharField(max_length=100)
    password2 =  models.CharField(max_length=100)
    USERNAME_FIELD = 'EmailId'

    def __str__(self):
        return self.EmailId



