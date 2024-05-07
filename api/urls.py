from django.urls import path
from api import views
urlpatterns = [
    path('createVendor',views.createVendor),
    path('vendordetails',views.VendorDetails),
    path('vendordetails/<int:pk>',views.VendorDetailsid)
]
