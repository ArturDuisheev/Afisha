from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/reviews/', views.ReviewListAPIView.as_view(), name='index'),
    path('api/v1/reviews/<int:pk>/', views.ReviewDetailAPIView.as_view(), name='detail'),
    path('api/v1/reviews/create/', views.ReviewCreateAPIView.as_view(), name='create'),
    path('api/v1/reviews/<int:pk>/update/', views.ReviewUpdateAPIView, name='update'),
    path('api/v1/reviews/<int:pk>/delete/', views.ReviewDeleteAPIView, name='delete'),

]