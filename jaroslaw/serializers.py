from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyJaroslaw


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyJaroslawSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyJaroslaw
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
