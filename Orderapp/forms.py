from django import forms


class OrderForm(forms.Form):
    what_are_you_ordering = forms.CharField(required=True)
    quantity = forms.IntegerField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    company = forms.CharField(required=True)
    address = forms.CharField(required=True)
    place_of_delivery = forms.CharField(required=True)
