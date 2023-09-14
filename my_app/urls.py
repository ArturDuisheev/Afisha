from django.urls import path

from . import views

urlpatterns = [

    # directors
    path('api/v1/directors/', views.DirectorListAPIView.as_view(), name='list-director'),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view(), name='detail-director'),
    path('api/v1/directors/create/', views.DirectorCreateAPIView.as_view(), name='create-director'),

    # movies
    path('api/v1/movies/', views.MovieListAPIView.as_view(), name='list-movie'),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view(), name='detail-movie'),
    path('api/v1/movies/create/', views.MovieCreateAPIView.as_view(), name='create-movie'),
    path('api/v1/movies/update/<int:id>/', views.MovieUpdateAPIView.as_view(), name='update-movie'),
    path('api/v1/movies/delete/<int:id>/', views.MovieDeleteAPIView.as_view(), name='delete-movie'),

]

