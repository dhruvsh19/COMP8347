from django import forms
# from django.contrib.auth.models import User
from myApp.models import Order, User


class InterestForm(forms.Form):
    interested = forms.CharField(label='Interested', widget=forms.RadioSelect(choices=[(1, 'yes'), (0, 'no')]))
    levels = forms.IntegerField(min_value=1, max_value=10, initial=1)
    comments = forms.CharField(
            widget=forms.Textarea(attrs={'cols': '30', 'rows': '15'}),
            label='Additional Comments', required=False)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {
            'student': forms.RadioSelect,
            'order_date': forms.SelectDateWidget
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]