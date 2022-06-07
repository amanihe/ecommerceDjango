from functools import partial
from pickle import FALSE, TRUE
import statistics
from urllib import response
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import Order
from rest_framework.response import Response

from Order.models import T_Facture, T_Order
from Order.serializers import *
#from django.core.mail import send_mail

from django.core.files.storage import default_storage
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from rest_framework.renderers import JSONRenderer

from Products.serializers import S_Product

method_decorator(csrf_protect)
# Create your views here.


@csrf_exempt
def Crud_Order(request, id=0):
    if request.method == 'GET':
        order = T_Order.objects.all()
        serializer = OrderSerializer(order, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        order_data = JSONParser().parse(request)
        serializer = OrderSerializer(data=order_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)

        return JsonResponse("Failed to Add order ", safe=False)
    elif request.method == 'PUT':
        order_data = JSONParser().parse(request)
        order = T_Order.objects.get(Ord_Id=order_data['Ord_Id'])
        serializer = OrderSerializer(order, data=order_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        order = T_Order.objects.get(Ord_Id=id)
        order.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def Crud_orderLigne(request, id=0):
    if request.method == 'GET':
        orderLigne = T_OrderLigne.objects.all()
        serializer = OrderLigneSerializer(orderLigne, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':

        orderLigne_data = JSONParser().parse(request)
        storet = T_OrderLigne.objects.filter(Order=orderLigne_data['Order'])
        store = OrderLigneSerializer(storet, many=True)
        for i in store.data:
            # print(orderLigne_data["Product"])
           # print(i['Product'])
            if (orderLigne_data["Product"] == i['Product']):
                print(i)
                return JsonResponse("you have already this product in cart", safe=False)

        serializer = OrderLigneSerializer(data=orderLigne_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("add successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        orderLigne_data = JSONParser().parse(request)
        orderLigne = T_OrderLigne.objects.get(
            OrdLign_Id=orderLigne_data['OrdLign_Id'])
        serializer = OrderLigneSerializer(orderLigne, data=orderLigne_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        orderLigne = T_OrderLigne.objects.get(OrdLign_Id=id)
        ser = OrderLigneSerializer(orderLigne)
        orderLigne.delete()
        # tester si panier est vide alors effacer le dernier ligne et effacer tout le panier
        allOrderLigne = T_OrderLigne.objects.filter(Order=ser.data['Order'])
        all = OrderLigneSerializer(allOrderLigne, many=True)
        if(len(all.data) == 0):
            order = T_Order.objects.get(Ord_Id=ser.data['Order'])
            order.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def New_Order(request, id=0):
    if request.method == 'POST':
        order_data = JSONParser().parse(request)
        # serializer = OrderSerializer(
        #    User=order_data["User"], Supplier=order_data["Supplier"], Ord_Type="customer", Ord_Status="created", Ord_Date=order_data["Ord_Date"],)
        serializer = OrderSerializer(
            User=0, Supplier=1, Ord_Type="customer", Ord_Status="created",)
        if serializer.is_valid():
            serializer.save()
            # serializerlign = OrderLigneSerializer(
            #    Order=serializer.Ord_Id, Product=order_data["Product"] ,Ord_Qte=1,)
           # if serializerlign.is_valid():
            #   serializerlign.save()
            #   return JsonResponse(" all Added  Successfully", safe=False)
            return JsonResponse("Added just order Successfully", safe=False)

        return JsonResponse("Failed to Add  all order ", safe=False)


@csrf_exempt
def Crud_Facture(request, id=0):
    if request.method == 'GET':
        facture = T_Facture.objects.all()
        serializer = FactureSerializer(facture, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        facture_data = JSONParser().parse(request)
        serializer = FactureSerializer(data=facture_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        facture_data = JSONParser().parse(request)
        facture = T_Facture.objects.get(Fact_Id=facture_data['Fact_Id'])
        serializer = FactureSerializer(facture, data=facture_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        facture = T_Facture.objects.get(Fact_Id=id)
        facture.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def get_allstore(request):
    if request.method == 'GET':
        store = T_Order.objects.all()
        serializer = OrderLigneSerializer(store, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def get_Cart(request, userId):
    try:
        store = T_Order.objects.filter(User=userId, Ord_Status="created")
        if request.method == 'GET':
            serializer = OrderSerializer(store, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def get_OrderByUser(request, userId):
    try:
        store = T_Order.objects.filter(User=userId).order_by('Ord_Date')
        if request.method == 'GET':
            serializer = OrderSerializer(store, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def get_OrderLigne(request, orderId):
    try:

        store = T_OrderLigne.objects.filter(
            Order=orderId).order_by('Create_at')
        if request.method == 'GET':
            serializer = OrderLigneSerializer(store, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def get_OrderHistory(request, orderId):
    try:

        T = {}

        
        X = {}
        Z = []
        allOrder = T_Order.objects.get(Ord_Id=orderId)
        ordSerialize = OrderSerializer(allOrder)
        #for i in ordSerialize.data:
        print(ordSerialize.data['Ord_Id'])
        T['Ord_Id'] = ordSerialize.data['Ord_Id']
        T['Ord_Date'] = ordSerialize.data['Ord_Date'][ : 10]
        T['Ord_Status'] = ordSerialize.data['Ord_Status']
        print(T)
        # if(['Ord_Type']=='customer'):
        allOrderLign = T_OrderLigne.objects.filter(Order=ordSerialize.data['Ord_Id'])
        ordLignSerialize = OrderLigneSerializer(allOrderLign, many=True)
        X={}
        V = []
        for j in ordLignSerialize.data:
            P = {}
                
            print(j['Product'])
            product = T_Product.objects.get(Prod_Id=j['Product'])
            S_Prod = S_Product(product)
            P['Ord_Qte'] = j['Ord_Qte']
            P['Prod_Name'] = S_Prod.data['Prod_Name']
            P['Prod_Marque'] = S_Prod.data['Prod_Marque']
            P['Prod_Price'] = S_Prod.data['Prod_Price']
            P['Prod_Img'] = S_Prod.data['Prod_Img']
            V.append(P)
        print(V)
        X[0] = T
        X[1] = V
        # print(Z)
        if request.method == 'GET':
            return JsonResponse(X, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def edit_OrderLigne(request, Id):

    Vqte = JSONParser().parse(request)
    item = T_OrderLigne.objects.get(OrdLign_Id=Id)
    item.Ord_Qte = Vqte['Ord_Qte']
    item.save(update_fields=['Ord_Qte'])
    return JsonResponse(item.Ord_Qte, safe=False)


@csrf_exempt
def create(self, request, *args, **kwargs):
    user = request.user
    order = get_object_or_404(T_Order, User=user)
    product = get_object_or_404(T_Product, pk=request.data["product"])
    current_item = T_OrderLigne.objects.filter(Order=order, Product=product)
    quantity = int(request.data["quantity"])
   # if user == product.user:
    #   raise PermissionDenied("This Is Your Product")

   # if current_item.count() > 0:
    #    raise NotAcceptable("You already have this item in your shopping cart")

    # try:
    #    quantity = int(request.data["quantity"])
  #  except Exception as e:
   #     raise ValidationError("Please Enter Your Quantity")

   # if quantity > product.quantity:
    #    raise NotAcceptable("You order quantity more than the seller have")

    order_item = T_OrderLigne(cart=order, product=product, Ord_Qte=quantity)
    order_item.save()
    serializer = OrderLigneSerializer(order_item)
    total = float(product.price) * float(quantity)
    order.save()
    if serializer.is_valid():
        serializer.save()
        return JsonResponse("Updated Successfully", safe=False)

    return JsonResponse(serializer.data, status=statistics.HTTP_201_CREATED)
