from rest_framework import serializers
from Order.models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = T_Order
        fields = ("Ord_Id", "User", "Supplier",
                  "Ord_Type", "Ord_Status", "Ord_Date")


class OrderLigneSerializer(serializers.ModelSerializer):
    class Meta:
        model = T_OrderLigne
        fields = ("OrdLign_Id", "Order", "Product", "Ord_Qte", "Create_at")


class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = T_Facture
        fields = ("Fact_Id", "Fact_Num", "Fact_OrderCost",
                  "Fact_Discount", "Fact_CostFinal", "Fact_Type", "Create_at")
