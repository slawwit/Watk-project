from django.contrib.auth.models import User
from rest_framework import serializers

from rudna.models import LicznikBazowyRudna


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyRudnaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyRudna
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
