# todo/serializers.py

from rest_framework import serializers
from .models import Dash

class DashSerializer(serializers.ModelSerializer):
  class Meta:
    model = Dash
    fields = ('label','value')