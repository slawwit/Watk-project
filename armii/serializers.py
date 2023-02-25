from django.contrib.auth.models import User
from rest_framework import serializers

from .models import LicznikBazowyArmii


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LicznikBazowyArmiiSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicznikBazowyArmii
        fields = ['id', 'ID_DYS', 'ID_WAZ', 'SYMBOL', 'TOTAL', 'ARTYKUL', 'KIEDY']
