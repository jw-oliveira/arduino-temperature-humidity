from rest_framework import serializers
from .models import Records


class RecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ['id', 'temperature', 'humidity', 'registry_date']