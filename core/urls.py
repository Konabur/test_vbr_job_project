from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    CreateUserView,
    OrganizationListCreateView,
    OrganizationRetrieveUpdateView,
    EventListCreateView,
    EventRetrieveUpdateView
)

urlpatterns = [
    path('api/create_user/', CreateUserView.as_view(), name='create_user'),
    path('api/organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('api/organizations/<int:pk>/', OrganizationRetrieveUpdateView.as_view(), name='organization-retrieve-update'),
    path('api/events/', EventListCreateView.as_view(), name='event-list-create'),
    path('api/events/<int:pk>/', EventRetrieveUpdateView.as_view(), name='event-retrieve-update'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
