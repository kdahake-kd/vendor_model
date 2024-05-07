from rest_framework import serializers
from api import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Vendor
        fields='__all__'

    # def create(self, validated_data):
    #     return super().create(validated_data)

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.PurchaseOrder
        fields='__all__'

class HistoricalPerformanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.HistoricalPerformanceModel
        fields='__all__'