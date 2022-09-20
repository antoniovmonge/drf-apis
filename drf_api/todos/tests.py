from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Todo

User = get_user_model()


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="First Todo", body="A body of text here")
        cls.user = User.objects.create_user(
            email="testuser@email.com", password="testpass123"
        )

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")

    def test_api_listview(self):
        client = APIClient()
        client.login(email="testuser@email.com", password="testpass123")
        response = client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, self.todo)

    def test_api_detailview(self):
        client = APIClient()
        client.login(email="testuser@email.com", password="testpass123")
        response = client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        self.assertContains(response, "First Todo")
