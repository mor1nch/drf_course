from rest_framework import status
from rest_framework.test import APITestCase


class UsersTestCase(APITestCase):

    def test_UserRegister(self):
        data = {
            "username": "test",
            "password": "test",
            "password_confirm": "test",
            "chat_id": 1234567890
        }
        response = self.client.post('/users/register/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['username'], 'test')
