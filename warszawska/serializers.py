from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyWarszawska


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyWarszawskaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyWarszawska
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
