from rest_framework import serializers

from .models import Review, Case, Callback, Event


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class CaseFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = ("id","title","objective","banner")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Callback
        fields = "__all__"
