from django.db import models

# Create your models here.

class ShipmentFormModel(models.Model):
    shipment_id = models.AutoField(primary_key=True)
    shipment_name = models.CharField(max_length=100)
    shipment_date = models.DateField(auto_now_add=True)
    shipment_status = models.BooleanField(default=False)
    shipment_description = models.TextField()

    def __str__(self):
        return self.shipment_name
    
    
