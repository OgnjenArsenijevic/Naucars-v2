import django_filters
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import models
from django import forms

from .models import Ad


class AdFilter(django_filters.FilterSet):

    price_from = django_filters.NumberFilter(field_name='price', lookup_expr='gt', validators=[MinValueValidator(0), MaxValueValidator(50000001)])
    price_to = django_filters.NumberFilter(field_name='price', lookup_expr='lt', validators=[MinValueValidator(0), MaxValueValidator(50000001)])
    production_year_from = django_filters.NumberFilter(field_name='productionYear', lookup_expr='gt', validators=[MinValueValidator(1899), MaxValueValidator(2020)])
    production_year_to = django_filters.NumberFilter(field_name='productionYear', lookup_expr='lt', validators=[MinValueValidator(1899), MaxValueValidator(2020)])
    kilometers_from = django_filters.NumberFilter(field_name='kilometers', lookup_expr='gt', validators=[MinValueValidator(0), MaxValueValidator(2000001)])
    kilometers_to = django_filters.NumberFilter(field_name='kilometers', lookup_expr='lt', validators=[MinValueValidator(0), MaxValueValidator(2000001)])
    kW_from = django_filters.NumberFilter(field_name='kW', lookup_expr='gt', validators=[MinValueValidator(0), MaxValueValidator(7001)])
    kW_to = django_filters.NumberFilter(field_name='kW', lookup_expr='lt', validators=[MinValueValidator(0), MaxValueValidator(7001)])
    cm3_from = django_filters.NumberFilter(field_name='cm3', lookup_expr='gt', validators=[MinValueValidator(0), MaxValueValidator(10001)])
    cm3_to = django_filters.NumberFilter(field_name='cm3', lookup_expr='lt', validators=[MinValueValidator(0), MaxValueValidator(10001)])

    class Meta:
        model = Ad
        fields = ['manufacturer', 'model', 'color']
