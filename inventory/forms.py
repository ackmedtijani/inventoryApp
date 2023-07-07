from django import forms
from .models import Purchase , Product  , Order

class ProductForm(forms.ModelForm):
    name = forms.CharField(label='Name' ,
                        widget=forms.TextInput(attrs={'placeholder': 'Name'}), 
                        required=True)
    quantity_per_pack = forms.IntegerField(label='Quantity Per Pack' ,
                        widget=forms.NumberInput(attrs={'placeholder': 'Quantity Per Pack'})
                           ,required=False)
    quantity_per_unit = forms.IntegerField(label='Quantity Per Unit' ,
                        widget=forms.NumberInput(attrs={'placeholder': 'Quantity Per Unit'})
                           ,required=False)
    price_per_quantity = forms.IntegerField(label='Price Per Quantity' ,
                        widget=forms.NumberInput(attrs={'placeholder': 'Price Per Quantity'})
                           ,required=True)
    price_per_unit = forms.IntegerField(label='Price Per Unit' ,
                widget=forms.NumberInput(attrs={'placeholder': 'Price Per Unit'})
                           ,required=True)


    class Meta:
        model = Product
        fields = '__all__'


class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = 'price'
        