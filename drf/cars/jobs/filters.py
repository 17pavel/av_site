import django_filters
from .models import Jobs


class JobFilter(django_filters.FilterSet):
    class Meta:
        model = Jobs
        fields = ["date", "period"]