from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from parsley.decorators import parsleyfy
from .models import Ad


@parsleyfy
class AdForm(forms.ModelForm):

    class Meta:
        model = Ad
        fields = ['manufacturer', 'model', 'price', 'productionYear', 'kilometers', 'color', 'kW', 'cm3', 'image', 'contactNumber']
        parsley_extras = {
            'manufacturer': {
                'minlength': "1",
                'maxlength': "30",
                'error-message': "Please enter valid manufacturer",
            },
            'model': {
                'minlength': "1",
                'maxlength': "20",
                'error-message': "Please enter valid model",
            },
            'price': {
                'min': "1",
                'max': "50000000",
                'error-message': "Please enter valid price",
            },
            'productionYear': {
                'min': "1900",
                'max': "2019",
                'error-message': "Please enter valid production year",
            },
            'kilometers': {
                'min': "1",
                'max': "2000000",
                'error-message': "Please enter valid kilometers",
            },
            'color': {
                'maxlength': "20",
                'error-message': "Please enter valid color",
            },
            'kW': {
                'min': "1",
                'max': "7000",
                'error-message': "Please enter valid kW",
            },
            'cm3': {
                'min': "1",
                'max': "10000",
                'error-message': "Please enter valid cm3",
            },
            'contactNumber': {
                'minlength': '7',
                'maxlength': '15',
                'error-message': 'Please enter valid contact number'
            }
        }


@parsleyfy
class AdSearchForm(forms.ModelForm):
    price_From = forms.IntegerField(validators=[MaxValueValidator(50000000), MinValueValidator(1)])
    price_To = forms.IntegerField(validators=[MaxValueValidator(50000000), MinValueValidator(1)])
    production_Year_From = forms.IntegerField(validators=[MaxValueValidator(2019), MinValueValidator(1900)])
    production_Year_To = forms.IntegerField(validators=[MaxValueValidator(2019), MinValueValidator(1900)])
    Kilometers_From = forms.IntegerField(validators=[MaxValueValidator(2000000), MinValueValidator(1)])
    Kilometers_To = forms.IntegerField(validators=[MaxValueValidator(2000000), MinValueValidator(1)])
    kW_From = forms.IntegerField(validators=[MaxValueValidator(7000), MinValueValidator(1)])
    kW_To = forms.IntegerField(validators=[MaxValueValidator(7000), MinValueValidator(1)])
    cm3_From = forms.IntegerField(validators=[MaxValueValidator(10000), MinValueValidator(1)])
    cm3_To = forms.IntegerField(validators=[MaxValueValidator(10000), MinValueValidator(1)])

    class Meta:
        model = Ad
        fields = ['price_From', 'price_To', 'production_Year_From', 'production_Year_To', 'Kilometers_From', 'Kilometers_To',
                  'kW_From', 'kW_To', 'cm3_From', 'cm3_To']
        parsley_extras = {
            'price_From': {
                'minlength': "1",
                'maxlength': "50000000",
                'error-message': "Please enter valid price",
            }
        }
