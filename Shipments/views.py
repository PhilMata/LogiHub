from django.shortcuts import render
from .forms import ShipmentForm

# Create your views here.

def add_shipment(request):
    form = ShipmentForm()
    context = {
        'form': form}
    return render(request, 'Shipments/shipment_form.html',context)


def dash_shipment(request):
    return render(request, 'Shipment/dash_shipment.html')