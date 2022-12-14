from factory import Faker
from factory.django import DjangoModelFactory

from .models import Todo


class TodoFactory(DjangoModelFactory):
    class Meta:
        model = Todo

    title = Faker("sentence")
    body = Faker("text")
