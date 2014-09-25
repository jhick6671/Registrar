from apps.students import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Students
        fields = ('id', 'name', 'gpa', 'address')


