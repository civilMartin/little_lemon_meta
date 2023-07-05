from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import MenuItem, Booking


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta():
        model = MenuItem
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = '__all__'


class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        # Return the group name
        return value.name


class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')
