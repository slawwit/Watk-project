from django.contrib.auth.models import User
from rest_framework import serializers

from wola.models import LicznikBazowyWola


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyWolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyWola
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
