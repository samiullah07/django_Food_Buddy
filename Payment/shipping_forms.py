from django import forms
from .models import ShippingAddress

class ShipppingForm(forms.ModelForm):
	full_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False )
	email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email'}), required=False )
	address = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 2'}), required=False)
	city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),required=False )
	zip_code = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=False)
	country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country'}), required=False)

	class Meta:
		model = ShippingAddress
		fields = ['full_name', 'email', 'address', 'city','zip_code', 'country']
		exclude = ["user"]







class PaymentForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Card Number', 'class': 'form-control'}))
    expiration_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM / YY', 'class': 'form-control'}))
    cvv = forms.CharField(max_length=3, widget=forms.PasswordInput(attrs={'placeholder': 'CVV', 'class': 'form-control'}))
    name_on_card = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name on Card', 'class': 'form-control'}))


