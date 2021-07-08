from rest_framework import serializers
from .models import Auto


class AutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auto
        fields = ('id', 'name', 'mark')