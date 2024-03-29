from rest_framework import serializers
from .models import Subscriber, Content

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = '__all__'

class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'

class UpdateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ["title", "body"]
