from rest_framework import permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView

from user_actions import models as uc_m
from user_actions import serializers as uc_s


class ReviewListAPIView(ListAPIView):
    queryset = uc_m.Review.objects.all()
    serializer_class = uc_s.ReviewSerializer
    permission_classes = [permissions.AllowAny]


class ReviewDetailAPIView(RetrieveAPIView):
    serializer_class = uc_s.ReviewSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'id'

    def get_object(self):
        return uc_m.Review.objects.get(id=self.kwargs['id'])


class ReviewCreateAPIView(CreateAPIView):
    queryset = uc_m.Review.objects.all()
    serializer_class = uc_s.ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReviewUpdateAPIView:
    pass


class ReviewDeleteAPIView:
    pass