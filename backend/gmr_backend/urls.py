
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView)
from .views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    # Path to obtain a new access and refresh token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # Submit your refresh token to this path to obtain a new access token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Register a new user
    path('register/', register, name='register_view'),
]
