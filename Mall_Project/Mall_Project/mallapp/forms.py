from django import forms
from mallapp.models import shopdetails,manageoffers


class newshopdetailsupdate(forms.ModelForm):
    class Meta:
        model = shopdetails
        fields = '__all__'


class newmanageoffersupdate(forms.ModelForm):
    class Meta:
        model = manageoffers
        fields = '__all__'        