from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CreateUserView

urlpatterns = [
    path('api/create_user/', CreateUserView.as_view(), name='create_user'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
