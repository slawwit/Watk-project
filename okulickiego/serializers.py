from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyOkulickiego


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyOkulickiegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyOkulickiego
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
