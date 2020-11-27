from django import forms
 
class checkboxfield(forms.Form):
	check_box = forms.BooleanField(required=False)