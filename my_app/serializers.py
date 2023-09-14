from django.db.models import Avg
from rest_framework import serializers as ser

from my_app import models as my_app_models
from user_actions.models import Review
from user_actions.serializers import ReviewSerializer


class DirectorSerializer(ser.ModelSerializer):
    created_at = ser.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = my_app_models.Director
        fields = 'name created_at'.split()


class MovieSerializer(ser.ModelSerializer):
    reviews = ReviewSerializer(many=True, required=False)
    average_rating = ser.DecimalField(max_digits=3, decimal_places=2, read_only=True, required=False)
    created_at = ser.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = my_app_models.Movie
        fields = 'id title description duration reviews average_rating director created_at'.split()

    def to_representation(self, instance):
        # Используйте annotate для получения среднего рейтинга и отзывов к каждому фильму
        queryset = Review.objects.filter(movie=instance)
        avg_rating = queryset.aggregate(Avg('stars'))['stars__avg']

        # Сериализуйте данные фильма и добавьте средний рейтинг
        data = super().to_representation(instance)
        data['average_rating'] = avg_rating
        data['reviews'] = ReviewSerializer(queryset, many=True).data
        return data





