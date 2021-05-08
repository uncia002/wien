# coding: utf-8

from rest_framework import serializers

from .models import Preset


class PresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preset
        fields = ('title',)
