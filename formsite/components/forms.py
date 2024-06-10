# forms.py
from django import forms

COMPONENT_CHOICES = [
    ('gpu', 'GPU'),
    ('cpu', 'CPU'),
    ('psu', 'PSU'),
    ('motherboard', 'Motherboard'),
]

class ComponentChoiceForm(forms.Form):
    component_type = forms.ChoiceField(choices=COMPONENT_CHOICES, required=True, widget=forms.Select(attrs={'id': 'component_type'}))

class GPUFilterForm(forms.Form):
    price_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    power_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    gaming_performance_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    memory_size_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    core_clock_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))

class CPUFilterForm(forms.Form):
    price_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    power_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    gaming_performance_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    cores_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    clock_speed_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))

class PSUFilterForm(forms.Form):
    price_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    power_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    efficiency_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))

class MotherboardFilterForm(forms.Form):
    price_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    power_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
    form_factor_weight = forms.DecimalField(max_digits=5, decimal_places=2, required=False, initial=1, widget=forms.NumberInput(attrs={'value': 1}))
