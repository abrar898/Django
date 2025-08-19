from rest_framework import serializers
from .models import *
# create a user requires three given things
class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model=React
        fields=['employee','department']