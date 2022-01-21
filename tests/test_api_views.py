import logging

from django.contrib.auth.models import User
from django.test import RequestFactory
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from authentication.models import UserVerificationRequest
from config.models import Config
from general.utils import create_username_from_email


class ConfigAPITestCase(APITestCase):
    def setUp(self):
        self.email = 'testuser@helloworld.com'
        self.password_raw = 'testpass'
        self.username = create_username_from_email(self.email)
        self.user = User.objects.create_user(
            email='testuser@helloworld.com',
            password=self.password_raw,
            username=self.username
        )
        UserVerificationRequest.objects.create(email=self.user.email, user=self.user, used=True, is_active=False)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.request = RequestFactory()
        self.request.user = self.user
        logging.disable(logging.CRITICAL)

    def tearDown(self):
        logging.disable(logging.NOTSET)

    def test_get(self):
        config = Config.objects.create(name='force_update', value=True, data_type=Config.TYPE_BOOL)
        response = self.client.get(reverse('init'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(config.name in response.json())
        self.assertEqual(response.json()[config.name], config.value)
