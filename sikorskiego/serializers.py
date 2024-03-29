from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowySikorskiego


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowySikorskiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowySikorskiego
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
