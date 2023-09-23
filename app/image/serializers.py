"""
Serializers for recipe APIs
"""
from rest_framework import serializers

from core.models import Image


class ImageSerializer(serializers.ModelSerializer):
    """Serializer for Images."""

    class Meta:
        model = Image
        fields = ['id', 'user', 'image']
        read_only_fields = ['id']
