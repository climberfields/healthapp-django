from rest_framework import serializers
from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    features = serializers.PrimaryKeyRelatedField(many=True, allow_null=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'name', 'photo_url', 'features',)