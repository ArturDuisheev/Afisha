from rest_framework import serializers as ser
from django.db.models import Avg

from user_actions import models as user_actions_models


class ReviewSerializer(ser.ModelSerializer):
    created_at = ser.DateTimeField(format='%Y-%m-%d', read_only=True)

    class Meta:
        model = user_actions_models.Review
        fields = 'text movie stars created_at'.split()
