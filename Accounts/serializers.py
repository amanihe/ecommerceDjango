from rest_framework import serializers
from .models import *



class S_User(serializers.ModelSerializer):
    class Meta:
        model = T_User
        fields = ("U_Id", "U_FirstName","U_LastName","U_Tel","U_Statut", "U_Email","U_Pwd","U_Admin","U_Client","U_Supplier")
class S_Address(serializers.ModelSerializer):
    class Meta:
        model = T_Address
        fields = ("Adr_Id","Adr_Name","Adr_Ville","Adr_Province","Adr_Pays","Adr_Default","User")


class S_Request(serializers.ModelSerializer):
    class Meta:
        model = T_Request
        fields = ("Req_Id",  "User","Req_Type","Req_Result")