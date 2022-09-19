from factory import Faker
from factory.django import DjangoModelFactory

from .models import Book


class BookFactory(DjangoModelFactory):
    class Meta:
        model = Book

    title = Faker("sentence")
    subtitle = Faker("sentence")
    author = Faker("name")
    isbn = Faker("isbn13")
