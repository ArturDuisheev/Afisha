from django.db.models import Avg
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from my_app import models as my_app_models
from my_app import serializers as my_app_serializers

"""Режиссер"""


class DirectorListAPIView(ListAPIView):
    queryset = my_app_models.Director.objects.all()
    serializer_class = my_app_serializers.DirectorSerializer


class DirectorDetailAPIView(RetrieveAPIView):
    queryset = my_app_models.Director.objects.all()
    serializer_class = my_app_serializers.DirectorSerializer
    lookup_field = "id"


class DirectorCreateAPIView(CreateAPIView):
    queryset = my_app_models.Director.objects.all()
    serializer_class = my_app_serializers.DirectorSerializer


class DirectorUpdateAPIView(UpdateAPIView):
    queryset = my_app_models.Director.objects.all()
    serializer_class = my_app_serializers.DirectorSerializer
    lookup_field = "id"


class DirectorDeleteAPIView(DestroyAPIView):
    queryset = my_app_models.Director.objects.all()
    lookup_field = "id"


"""Фильм"""


class MovieListAPIView(ListAPIView):
    queryset = my_app_models.Movie.objects.all()
    serializer_class = my_app_serializers.MovieSerializer


class MovieDetailAPIView(RetrieveAPIView):
    queryset = my_app_models.Movie.objects.all()
    serializer_class = my_app_serializers.MovieSerializer
    lookup_field = "id"


class MovieCreateAPIView(CreateAPIView):
    queryset = my_app_models.Movie.objects.all()
    serializer_class = my_app_serializers.MovieSerializer


class MovieUpdateAPIView(UpdateAPIView):
    queryset = my_app_models.Movie.objects.all()
    serializer_class = my_app_serializers.MovieSerializer
    lookup_field = "id"


class MovieDeleteAPIView(DestroyAPIView):
    queryset = my_app_models.Movie.objects.all()
    lookup_field = "id"




