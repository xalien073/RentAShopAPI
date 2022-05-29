from dataclasses import field
from rest_framework import serializers
from .models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopImage
        fields = "__all__"

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"
        depth = 1

class NewShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = "__all__"

  