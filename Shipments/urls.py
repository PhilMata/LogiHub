from django.urls import path
from . import views

urlpatterns = [
    path("shipments/",views.add_shipment, name="add_shipment"),
    path('shipment/dashboard/',views.dash_shipment, name="dash_shipment"),
]


