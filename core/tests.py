from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Organization, Event

class ApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )
        self.organization_data = {
            'title': 'Test Organization',
            'description': 'Test Organization Description',
            'address': 'Test Organization Address',
            'postcode': '12345'
        }
        self.event_data = {
            'title': 'Test Event',
            'description': 'Test Event Description',
            'organizations': [],
            'date': '2024-01-20T12:00:00Z'
        }

    def get_access_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_organization_api(self):
        # Получение токена
        token = self.get_access_token()

        # Создание организации
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(reverse('organization-list-create'), self.organization_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        organization_id = response.data['id']

        # Получение списка организаций
        response = self.client.get(reverse('organization-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Обновление организации
        updated_organization_data = {
            'title': 'Updated Organization Title',
            'description': 'Updated Organization Description',
            'address': 'Updated Organization Address',
            'postcode': '54321'
        }
        response = self.client.put(reverse('organization-retrieve-update', args=[organization_id]), updated_organization_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Organization Title')

    def test_event_api(self):
        # Создание токена
        token = self.get_access_token()

        # Создание организации для использования в мероприятии
        organization = Organization.objects.create(**self.organization_data)

        # Создание мероприятия
        self.event_data['organizations'] = [organization.id]
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        response = self.client.post(reverse('event-list-create'), self.event_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        event_id = response.data['id']

        # Получение списка мероприятий
        response = self.client.get(reverse('event-list-create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Обновление мероприятия
        updated_event_data = {
            'title': 'Updated Event Title',
            'description': 'Updated Event Description',
            'organizations': [organization.id],
            'date': '2024-01-21T14:00:00Z'
        }
        response = self.client.put(reverse('event-retrieve-update', args=[event_id]), updated_event_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Event Title')
