from rest_framework import serializers
from Products.models import *


class S_Category(serializers.ModelSerializer):
    class Meta:
        model = T_Category
        fields = ("Categ_Id", "Categ_Name", "Categ_Parent","Create_at")


class S_Product(serializers.ModelSerializer):
    class Meta:
        model = T_Product
        fields = (
            "Prod_Id",
            "Prod_Name",
            "Prod_Description",
            "Prod_Marque",
            "Prod_Price",
            "Prod_Quantity",
            "Prod_Img",
            "category",
            "Create_at"
        )

class S_Characteristic(serializers.ModelSerializer):
    class Meta:
        model = T_Characteristic
        fields = (
            "Carec_Id", "Carecteristique", "category", "Create_at" )

class S_Carac_detail(serializers.ModelSerializer):
    class Meta:
        model = T_Carac_detail
        fields = (
            "Carac_Detail_Id", "Carac_Detail", "Carac_Id" )

class S_Carac_Product(serializers.ModelSerializer):
    class Meta:
        model = T_Carac_Product
        fields = (
            "Carec_Prod_Id", "Prod_Id", "Carec_Id", "Carac_Detail" )

            

class S_ProductImg(serializers.ModelSerializer):
    class Meta:
        model = T_ProductImg
        fields = (
            "product", "url" )

