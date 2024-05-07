from django.shortcuts import render,get_list_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from api import serializer,models
import json
from django.http import HttpResponse
# Create your views here.

class VendorAPIViewSet():
    pass



@api_view(['POST'])
def createVendor(request):
    body=json.loads(request.body)
    print("body we got",body)
    response=serializer.VendorSerializer(data=body)
    print('no respone got',response)

    if response.is_valid():
        print("valid data")
        inst=response.save()
        print('inst save',inst)
        response=serializer.VendorSerializer(inst)
        return Response(response.data)
    return Response(response.errors)

@api_view()
def VendorDetails(request):
    data=models.Vendor.objects.all()
    response=serializer.VendorSerializer(data,many=True)
    return Response(response.data)


@api_view()
def VendorDetailsid(request,pk):
     vendor=get_list_or_404(models.Vendor,pk=pk)
     responce=serializer.VendorSerializer(vendor,many=True)
     

     return Response(responce.data)

