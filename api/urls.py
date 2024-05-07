from django.urls import path
from api import views
# from api.views import CreateVendorView


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet
from django.urls import re_path
from rest_framework import routers

router = routers.SimpleRouter()
router.register("vendors", views.VendorViewSet, basename="Vendors")
router.register("purchase_orders",views.PurchaseOrder,basename="purchase_orders")


urlpatterns = [
    re_path("^", include(router.urls)),
    # path('createVendor',views.createVendor),
    # path('createvendorclass',CreateVendorView),
    # path('vendordetails',views.VendorDetails),
    # path('vendordetails/<int:pk>',views.VendorDetailsid),
]
