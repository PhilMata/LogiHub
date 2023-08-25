from django import forms
from .models import ShipmentFormModel

class ShipmentForm(forms.ModelForm):
    class Meta:
        model = ShipmentFormModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })