from django.db import models

# Create your models here.

class Vendor(models.Model):
    name=models.CharField(max_length=255)
    contact_details=models.TextField()
    address=models.TextField()
    Vendor_code=models.CharField(max_length=256,unique=True)
    on_time_delivery_rate=models.FloatField(null=True,blank=True,default=0.0)
    quality_rating_avg=models.FloatField(null=True,blank=True,default=0.0)
    average_response_time=models.FloatField(null=True,blank=True,default=0.0)
    fulfillment_rate=models.FloatField(null=True,blank=True,default=0.0)

    def __str__(self) -> str:
        return self.name

class PurchaseOrder(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    )

    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=100,choices=STATUS_CHOICES)
    quality_rating = models.FloatField(null=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return self.po_number


class HistoricalPerformanceModel(models.Model):
    """
    This model stores historical data on vendor performance, enabling trend analysis.
    """
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def __str__(self) -> str:
        return self.vendor

    



