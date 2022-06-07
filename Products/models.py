from datetime import datetime
from msilib.schema import Class
from django.db import models
# Create your models here.


class T_Category(models.Model):
    Categ_Id = models.AutoField(primary_key=True)
    Categ_Name = models.CharField(max_length=100, unique=True)
    Categ_Parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
                                     )
    Create_at = models.DateTimeField(auto_now_add=True)


class T_Characteristic(models.Model):
    Carec_Id = models.AutoField(primary_key=True)
    Carecteristique = models.CharField(max_length=100, unique=True)
    category = models.ManyToManyField(T_Category, blank=False)
    Create_at = models.DateTimeField(auto_now_add=True)


class T_Carac_detail(models.Model):
    Carac_Detail_Id = models.AutoField(primary_key=True)
    Carac_Detail = models.CharField(max_length=100, unique=True)
    Carac_Id = models.ForeignKey(T_Characteristic,
                                 on_delete=models.CASCADE)

   # def get_absolute_url(self):
   # return reverse("products:category", kwargs={"name": self.name})


class T_Product(models.Model):
    Prod_Id = models.AutoField(primary_key=True)
    category = models.ForeignKey(T_Category,
                                 on_delete=models.CASCADE)
    Prod_Name = models.CharField(max_length=150)
    Prod_Description = models.TextField(
        max_length=500, default="Empty description.")
    Prod_Marque = models.TextField(max_length=500)

    Prod_Price = models.DecimalField(
        decimal_places=2, max_digits=20, default=0)

    # available quantity of given product
    Prod_Quantity = models.IntegerField(default=10)
    Prod_Img = models.CharField(max_length=100, unique=True, default="")
    #Prod_available =models.BooleanField(default=False)
    Create_at = models.DateTimeField(auto_now_add=True)

    @property
    def is_available(self):
        return self.Prod_Quantity > 0


class T_ProductImg(models.Model):
    product = models.ForeignKey(T_Product, on_delete=models.CASCADE)
    url = models.CharField(max_length=100, unique=True)


class T_Carac_Product(models.Model):
    Carec_Prod_Id = models.AutoField(primary_key=True)
    Prod_Id = models.ForeignKey(T_Product,
                                on_delete=models.CASCADE)
    Carec_Id = models.ForeignKey(T_Characteristic,
                                 on_delete=models.CASCADE)
    Carac_Detail = models.CharField(max_length=100, unique=True)


#from Accounts.models import T_Admin, T_Supplier
# class T_Stock(models.Model):
   # WHSE_Id = models.ForeignKey(T_Supplier,
  #                              on_delete=models.CASCADE)
   # Prod_Id = models.ForeignKey(T_Product,
   #                             on_delete=models.CASCADE)
   # Admin_Id = models.ForeignKey(T_Admin,
    #                            on_delete=models.CASCADE)
    #ST_qteActuel = models.IntegerField()
  #  ST_qteReserv = models.IntegerField()
