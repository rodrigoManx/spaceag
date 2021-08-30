from django.contrib.auth.models import User
from rest_framework import serializers
from .models import FieldWorker


class FieldWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldWorker
        fields = ('first_name', 'last_name', 'function', 'id')
