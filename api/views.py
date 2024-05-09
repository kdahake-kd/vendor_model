from rest_framework.decorators import action
from rest_framework.response import Response

from rest_framework import viewsets, status
from .models import *
from api.serializer import *


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(methods=["get"], detail=True, name="performance", url_name="performance")
    def performance(self, *args, **kwargs):
        vendor = self.get_object()
        historical_performance = vendor.historical_performance.last()
        serialized_data = HistoricalPerformanceModelSerializer(historical_performance).data

        return Response(serialized_data, status=status.HTTP_200_OK)


class PurchaseOrder(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    @action(methods=["post"], detail=True, name="acknowledge", url_name="acknowledge")
    def acknowledge(self, *args, **kwargs):
        po = self.get_object()
        request_data = AcknowledgementDateSerializer(data=self.request.data)
        if not request_data.is_valid():
            return Response(request_data.errors, status=status.HTTP_400_BAD_REQUEST)

        po.acknowledgment_date = request_data.validated_data.get("acknowledgment_date")
        po.save()

        return Response(PurchaseOrderSerializer(po).data, status=status.HTTP_200_OK)










