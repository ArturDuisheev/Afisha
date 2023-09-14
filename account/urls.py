from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from account import views as v

urlpatterns = [
    path('register/', v.UserRegistrationView.as_view(), name='register'),
    path('login/', v.UserLoginView.as_view(), name='login'),
    path('logout/', v.UserLogoutView.as_view(), name='logout'),
    path('profile/', v.UserProfileView.as_view(), name='profile'),
    path('confirm/', v.UserConfirmationView.as_view(), name='confirm-user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
