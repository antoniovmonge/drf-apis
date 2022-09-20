from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from drf_api.books.factories import BookFactory
from drf_api.books.models import Book


class Command(BaseCommand):
    help = "Seed database with sample data (Books)."

    @transaction.atomic
    def handle(self, *args, **options):
        if Book.objects.exists():
            raise CommandError(
                "This command cannot be run when any book exist, "
                + "to guard against accidental use on production."
            )
        self.stdout.write("Seeding database with books...")
        create_books()
        self.stdout.write("Done.")


def create_books():
    BookFactory.create_batch(5)
