from django.shortcuts import render,get_list_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from api import serializer,models
import json
from django.http import HttpResponse
from django.views.generic import CreateView
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from .models import *
from api.serializer import *
# Create your views here



class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class PurchaseOrder(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    







