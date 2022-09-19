from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from drf_api.books.models import Book

User = get_user_model()


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(
            title="Django for APIs",
            subtitle="Build web APIs with Python and Django",
            author="William S. Vincent",
            isbn="0-7475-3269-9",
        )
        cls.user = User.objects.create_user(
            email="testuser@email.com", password="testpass123"
        )

    def test_api_listview(self):
        client = APIClient()
        client.login(email="testuser@email.com", password="testpass123")
        # user = User.objects.get(email="testuser@email.com")
        # client.force_authenticate(user=user)
        response = client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
