from rest_framework import serializers
from .models import OrganizedLocation

class OrganizedLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizedLocation
        fields = '__all__'
