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
