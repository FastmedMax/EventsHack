from rest_framework import serializers

from .models import Review, Case, Callback, Event


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"
