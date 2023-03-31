from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyPodkarpacka


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyPodkarpackaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyPodkarpacka
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
