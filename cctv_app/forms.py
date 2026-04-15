from django import forms
from .models import PriceMaster


class CCTVPricingForm(forms.Form):
    camera = forms.ModelChoiceField(queryset=PriceMaster.objects.none())
    cable = forms.ModelChoiceField(queryset=PriceMaster.objects.none())
    recorder = forms.ModelChoiceField(queryset=PriceMaster.objects.none())
    channel = forms.ModelChoiceField(queryset=PriceMaster.objects.none())
    poe = forms.ModelChoiceField(queryset=PriceMaster.objects.none())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['camera'].queryset = PriceMaster.objects.filter(category='camera')
        self.fields['cable'].queryset = PriceMaster.objects.filter(category='cable')
        self.fields['recorder'].queryset = PriceMaster.objects.filter(category='recorder')
        self.fields['channel'].queryset = PriceMaster.objects.filter(category='channel')
        self.fields['poe'].queryset = PriceMaster.objects.filter(category='poe')