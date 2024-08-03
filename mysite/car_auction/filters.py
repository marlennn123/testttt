from django_filters.rest_framework import FilterSet
from .models import Car


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'category': ['exact'],
            'car_make': ['exact'],
            'model': ['exact'],
            'price': ['gt', 'lt']

        }