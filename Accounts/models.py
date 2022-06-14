from django.db import models


# class T_Company(models.Model):
#   C_Id = models.AutoField(primary_key=True)
#  C_Name = models.CharField(max_length=150)
#  C_Email = models.EmailField()

STATUT_CHOICES = (
    ('autre', 'autre'),
    ('professionnel', 'Professionnel'),
    ('personnel', 'Personnel')
)
class T_User(models.Model):
    U_Id = models.AutoField(primary_key=True)
    U_FirstName = models.CharField(max_length=150)
    U_LastName = models.CharField(max_length=150)
    U_Tel = models.CharField(max_length=150)
    U_Statut =models.CharField(max_length=120, choices=STATUT_CHOICES)
    U_Email = models.EmailField()
    U_Pwd = models.CharField(max_length=150)
    U_Admin = models.BooleanField()
    U_Client = models.BooleanField()
    U_Supplier = models.BooleanField()


class T_Address(models.Model):
    Adr_Id = models.AutoField(primary_key=True)

    Adr_Name = models.CharField(max_length=150)
    Adr_Ville = models.CharField(max_length=150)
    Adr_Province = models.CharField(max_length=150)
    Adr_Pays = models.CharField(max_length=150)
    Adr_Default = models.BooleanField()
    User = models.ForeignKey(
        T_User, on_delete=models.CASCADE)

# class T_Supplier(models.Model):
    # Sup_Id = models.AutoField(primary_key=True)
    # Sup_Name = models.CharField(max_length=100, unique=True)
    # Sup_Email = models.EmailField()
    # Sup_Pwd = models.CharField(max_length=100, unique=True)

# class T_Admin(models.Model):
    # Admin_Id = models.AutoField(primary_key=True)
    # Admin_Login = models.CharField(max_length=100, unique=True)
    # Admin_Pwd = models.CharField(max_length=100, unique=True)

# class T_Client(models.Model):
    # Clt_Id = models.AutoField(primary_key=True)
    # Clt_Nom = models.CharField(max_length=150)
    # Clt_Prenom = models.CharField(max_length=150)
    # Clt_NumTel = models.CharField(max_length=150)
    # Clt_Email = models.EmailField()
    # Clt_Pwd = models.CharField(max_length=150)


ORDER_TYPE_CHOICES = (
    ('supplier', 'Supplier'),
    ('admin', 'Admin')
)


class T_Request(models.Model):
    Req_Id = models.AutoField(primary_key=True)
    User = models.ForeignKey(
        T_User, on_delete=models.CASCADE, related_name='User_Request')
    Req_Type = models.CharField(max_length=120, choices=ORDER_TYPE_CHOICES)
    Req_Result = models.IntegerField(default=0)


# class T_Address(models.Model):
    # Adr_Id=models.AutoField(primary_key=True, serialize=False)
    # Adr_Name= models.CharField(max_length=150)
    # Adr_Ville= models.CharField(max_length=150)
    # Adr_Province= models.CharField(max_length=150)
    # Adr_Pays=models.CharField(max_length=150)
    # Adr_Default=models.BooleanField()
    # Clt_Id= models.ForeignKey(T_Client,
    #                    on_delete=models.CASCADE)


# class Access(models.Model):
    # Acc_Id = models.AutoField(primary_key=True)
    # Clt_Id = models.ForeignKey(Client, on_delete=models.CASCADE)
    # Acc_User = models.CharField(max_length=150)
    # Acc_Mdp = models.CharField(max_length=150)
    # Acc_Actif = models.BooleanField()


# Create your models here.
