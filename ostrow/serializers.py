from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyOstrow


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyOstrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyOstrow
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
