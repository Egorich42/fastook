from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['appointed_time']
        widgets = {
            'appointed_time': forms.TimeInput(format='%H:%M'),
        }
        exclude =['created',]
