from rest_framework import serializers
from api import models


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = '__all__'


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrder
        fields = '__all__'


class HistoricalPerformanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HistoricalPerformanceModel
        exclude = ["vendor", "id"
                   ]


class AcknowledgementDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PurchaseOrder
        fields = ["acknowledgment_date"
                  ]
