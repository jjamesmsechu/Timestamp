from django import forms


#How many Hours? Form
class hm_hours(forms.Form):
    num_hours = forms.CharField(label="Number of Days")

