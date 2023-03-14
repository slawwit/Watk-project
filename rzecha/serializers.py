from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyRzecha


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyRzechaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyRzecha
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
