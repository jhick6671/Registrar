from apps.locations import models, serializers
from rest_framework import generics
import django_filters

class IntegerListFilter(django_filters.Filter):
    def filter(self, queryset, value):
        if value not in (None, ''):
            integers = [int(v) for v in value.split(',')]
            return queryset.filter(**{'{}__{}'.format(self.name, self.lookup_type):integers})
        return queryset

class LocationFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')
    #fix this so the filter will search by name

    class Meta:
        model = models.Locations
        fields = ['id', 'name', 'city', 'address']

class UserCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Locations.objects.all()
    serializer_class = serializers.LocationSerializer
    filter_class = LocationFilter

