from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from drf_api.todos.factories import TodoFactory
from drf_api.todos.models import Todo


class Command(BaseCommand):
    help = "Seed database with sample data (Todos)."

    @transaction.atomic
    def handle(self, *args, **options):
        if Todo.objects.exists():
            raise CommandError(
                "This command cannot be run when any todo exist, "
                + "to guard against accidental use on production."
            )
        self.stdout.write("Seeding database with To-dos...")
        create_todos()
        self.stdout.write("Done.")


def create_todos():
    TodoFactory.create_batch(5)
