from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Accounts.models import *
from Accounts.serializers import *
#from django.core.mail import send_mail

from django.core.files.storage import default_storage
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

method_decorator(csrf_protect)
# Create your views here.


@csrf_exempt
def Crud_User(request, id=0):
    if request.method == 'GET':
        user = T_User.objects.all()
        serializer = S_User(user, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        test = T_User.objects.filter(U_Email=user_data['U_Email'])
        user = S_User(test, many=True)
        for i in user.data:
            if (user_data["U_Email"] == i['U_Email']):
                print(i)
                return JsonResponse("you have already account with this email", safe=False)
        serializer = S_User(data=user_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, safe=False)

        return JsonResponse("Failed to Add", safe=False)
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user = T_User.objects.get(U_Id=user_data['U_Id'])
        serializer = S_User(user, data=user_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        user = T_User.objects.get(U_Id=id)
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def get_Fnx(request, Id=0):
    try:
        user = T_User.objects.filter(U_Supplier=True)
        if request.method == 'GET':
            serializer = S_User(user, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)
@csrf_exempt
def get_User(request, Id):
    try:
        user = T_User.objects.filter(U_Id=Id)
        if request.method == 'GET':
            serializer = S_User(user, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def Crud_Address(request, id=0):
    if request.method == 'GET':
        address = T_Address.objects.all()
        serializer = S_Address(address, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        address_data = JSONParser().parse(request)
        test = T_Address.objects.filter(User=address_data['User'])
        address = S_Address(test, many=True)
        for i in address.data:
            if (address_data['Adr_Name'] == i['Adr_Name'] and address_data["Adr_Ville"] == i['Adr_Ville'] and address_data["Adr_Province"] == i['Adr_Province']and address_data["Adr_Pays"] == i['Adr_Pays']):
                print(i)
                return JsonResponse("you have already  this address", safe=False)
        serializer = S_Address(data=address_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse("Added Successfully", safe=False)

        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        address_data = JSONParser().parse(request)
        address = T_Address.objects.get(Adr_Id=address_data['Adr_Id'])
        serializer = S_Address(address, data=address_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        address = T_Address.objects.get(Adr_Id=id)
        address.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def get_Address_byUserId(request, userId):
    try:
        address = T_Address.objects.filter(User=userId)
        if request.method == 'GET':
            serializer = S_Address(address, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def edit_defaultAdress(request, Id):
    Vreq = JSONParser().parse(request)
    address = T_Address.objects.filter(User=Id)
    addressDefault = T_Address.objects.get(User=Id, Adr_Id=Vreq['Adr_Id'])
    if request.method == 'PUT':
        addressDefault.Adr_Default = True
        addressDefault.save(update_fields=['Adr_Default'])
        for i in address:
            if i.Adr_Id != Vreq['Adr_Id']:
                i.Adr_Default = False
                i.save(update_fields=['Adr_Default'])
                print(i.Adr_Default)
        return JsonResponse("default address updated", safe=False)
    return JsonResponse("error", safe=False)


@csrf_exempt
def Crud_Request(request, id=0):
    if request.method == 'GET':
        cltrequest = T_Request.objects.all()
        serializer = S_Request(cltrequest, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)
        test = T_Request.objects.filter(User=request_data['User'])
        req = S_Request(test, many=True)
        for i in req.data:
            if (request_data["User"] == i['User'] and request_data["Req_Type"] == i['Req_Type']):
                print(i)
                return JsonResponse("you have already  this request", safe=False)
        serializer = S_Request(data=request_data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse(serializer.data, safe=False)

        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'DELETE':
        cltrequest = T_Request.objects.get(Req_Id=id)
        cltrequest.delete()
        return JsonResponse("Deleted Successfully", safe=False)


@csrf_exempt
def edit_Request(request, Id):

    Vreq = JSONParser().parse(request)
    req = T_Request.objects.get(User=Id, Req_Type=Vreq['Req_Type'])
    req.Req_Result = Vreq['Req_Result']
    req.save(update_fields=['Req_Result'])
    return JsonResponse(req.Req_Result, safe=False)


@csrf_exempt
def get_Request(request, userId):
    try:
        req = T_Request.objects.filter(User=userId)
        if request.method == 'GET':
            serializer = S_Request(req, many=True)
            return JsonResponse(serializer.data, safe=False)
    except:
        return HttpResponse(status=404)


@csrf_exempt
def get_user(request, id):
    try:
        user = T_User.objects.get(pk=id)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = S_User(user)
        return JsonResponse(serializer.data)


@csrf_exempt
def check_login(request, email):
    try:
        user = T_User.objects.filter(U_Email=email)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = S_User(user, many=True)
        return JsonResponse(serializer.data, safe=False)
