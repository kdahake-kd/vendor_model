import datetime

from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import *


def get_vendor_performance_object(vendor_id):
    vendor_historical_performance_obj = HistoricalPerformanceModel.objects.filter(vendor_id=vendor_id).last()
    if vendor_historical_performance_obj is None:
        vendor_historical_performance_obj = HistoricalPerformanceModel(vendor_id=vendor_id)

    return vendor_historical_performance_obj


@receiver(post_save, sender=PurchaseOrder)
def update_ontime_delivery_rate(sender, instance, **kwargs):
    if instance.status == 'completed':
        # Count completed orders for this vendor
        completed_orders_count = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            status='completed'
        ).count()

        # Count completed orders delivered on or before delivery_date
        on_time_delivery_count = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            status='completed',
            delivery_date__lte=instance.delivery_date
        ).count()

        # Ensure no division by zero
        if completed_orders_count != 0:
            on_time_delivery_rate = on_time_delivery_count / completed_orders_count
        else:
            on_time_delivery_rate = 0.0

        # Update the vendor's on_time_delivery_rate field
        vendor_historical_performance_obj = get_vendor_performance_object(instance.vendor_id)
        today = datetime.datetime.now()
        vendor_historical_performance_obj.on_time_delivery_rate = on_time_delivery_rate
        vendor_historical_performance_obj.date = today
        vendor_historical_performance_obj.save()


@receiver(post_save, sender=PurchaseOrder)
def update_quality_rating_average(sender, instance, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        # Get all completed orders with quality ratings for this vendor
        completed_orders = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            status='completed',
            quality_rating__isnull=False
        )

        # Calculate the average quality rating
        total_quality_rating = completed_orders.aggregate(avg_quality_rating=Avg('quality_rating'))[
            'avg_quality_rating']
        if total_quality_rating is not None:  # Ensure there are completed orders with quality ratings
            # Update the vendor's quality_rating_avg field
            vendor_historical_performance_obj = get_vendor_performance_object(instance.vendor_id)
            today = datetime.datetime.now()
            vendor_historical_performance_obj.quality_rating_avg = total_quality_rating
            vendor_historical_performance_obj.date = today
            vendor_historical_performance_obj.save()


@receiver(post_save, sender=PurchaseOrder)
def update_average_response_time(sender, instance, **kwargs):
    if instance.acknowledgment_date:
        # Get all completed orders for this vendor
        completed_orders = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            status='completed',
            acknowledgment_date__isnull=False,
            issue_date__isnull=False
        )

        # Compute the time difference between issue_date and acknowledgment_date for each PurchaseOrder
        response_times = [(po.acknowledgment_date - po.issue_date).total_seconds() for po in completed_orders]

        # Calculate the average response time
        if response_times:
            average_response_time = sum(response_times) / len(response_times)
        else:
            average_response_time = 0.0

        vendor_historical_performance_obj = get_vendor_performance_object(instance.vendor_id)
        today = datetime.datetime.now()
        vendor_historical_performance_obj.average_response_time = average_response_time
        vendor_historical_performance_obj.date = today
        vendor_historical_performance_obj.save()


@receiver(post_save, sender=PurchaseOrder)
def update_fulfillment_rate(sender, instance, **kwargs):
    if instance.status == instance._previous_status:
        return

    total_pos_issued = PurchaseOrder.objects.filter(vendor=instance.vendor).count()

    # Count successfully fulfilled POs (completed without issues)
    fulfilled_pos_count = PurchaseOrder.objects.filter(
        vendor=instance.vendor,
        status='completed',
        issue_date__isnull=False,
        acknowledgment_date__isnull=False,
        delivery_date__isnull=False,
        quality_rating__isnull=True  # Assuming quality rating is not provided for successful fulfillment
    ).count()

    # Calculate fulfillment rate
    if total_pos_issued != 0:
        fulfillment_rate = fulfilled_pos_count / total_pos_issued
    else:
        fulfillment_rate = 0.0

    vendor_historical_performance_obj = get_vendor_performance_object(instance.vendor_id)
    today = datetime.datetime.now()
    vendor_historical_performance_obj.fulfillment_rate = fulfillment_rate
    vendor_historical_performance_obj.date = today
    vendor_historical_performance_obj.save()
