from django_filters.rest_framework import FilterSet
from django_filters import DateFromToRangeFilter, CharFilter
from advertisements.models import Advertisement


class AdvertisementFilter(FilterSet):
    """Фильтры для объявлений."""

    created_at = DateFromToRangeFilter()
    creator = CharFilter(field_name='creator', lookup_expr='exact')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'creator', ]
