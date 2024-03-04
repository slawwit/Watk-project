from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyJasionka


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyJasionkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyJasionka
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
