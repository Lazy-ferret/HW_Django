from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters, DateFromToRangeFilter, ModelChoiceFilter

from advertisements.models import Advertisement


User = get_user_model()


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    creator = ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at']
