from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyLezajsk


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyLezajskSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyLezajsk
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
