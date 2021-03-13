from django import forms

class addnodeform(forms.Form):
   city=forms.CharField(label="city")
   longitude=forms.CharField(label="longitude")
   laditude=forms.CharField(label="laditude")
