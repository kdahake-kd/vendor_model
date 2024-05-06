from django.contrib import admin
from api.models import *
# Register your models here.a

admin.site.register(Vendor)

admin.site.register(HistoricalPerformanceModel)

admin.site.register(PurchaseOrder)