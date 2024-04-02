from django import forms
class EnForm(forms.Form):
	name=forms.CharField(label="Name")
	email=forms.EmailField(label="Email")
	phone=forms.IntegerField(label="Phone")