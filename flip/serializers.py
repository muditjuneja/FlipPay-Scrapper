from rest_framework import serializers
from .models import Order, Item


class ItemSerializer(serializers.Serializer):
    """
    serializes an item of the order
    """
    name = serializers.CharField(max_length=50)
    properties = serializers.JSONField()
    price = serializers.FloatField()
    image_url = serializers.URLField()
    item_url = serializers.URLField()
    status = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Item(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.item_url = validated_data.get('item_url', instance.item_url)


class OrderSerializer(serializers.Serializer):
    """
    serializes an order instance
    """
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=50)
    value = serializers.FloatField()
    items = ItemSerializer(many=True)
    order_date = serializers.CharField(max_length=50)
    seller = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Order(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.value = validated_data.get('value', instance.value)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.delivery_date = validated_data.get('delivery_date',
                                           instance.delivery_date)
        instance.status = validated_data.get('status', instance.status)
        return instance
