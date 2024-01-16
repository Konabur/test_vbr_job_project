from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    CreateUserView,
    ObtainTokenAPIView,
    OrganizationListCreateView,
    OrganizationRetrieveUpdateView,
    EventListCreateView,
    EventRetrieveUpdateView
)


schema_view = get_schema_view(
    openapi.Info(
        title="Event Management API",
        default_version='v1',
        description="API for managing organizations and events",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="contact@yourapp.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/create_user/', CreateUserView.as_view(), name='create_user'),
    
    path('token/', ObtainTokenAPIView.as_view(), name='obtain_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('api/organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('api/organizations/<int:pk>/', OrganizationRetrieveUpdateView.as_view(), name='organization-retrieve-update'),
    
    path('api/events/', EventListCreateView.as_view(), name='event-list-create'),
    path('api/events/<int:pk>/', EventRetrieveUpdateView.as_view(), name='event-retrieve-update'),
    
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
