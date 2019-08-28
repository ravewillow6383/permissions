from rest_framework import serializers
from . import models

class ThingSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name')
        model = models.Thing