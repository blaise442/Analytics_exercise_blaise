from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Load patient data from CSV'

    def handle(self, *args, **options):
        # TODO: load patient data from CSV into models
        pass
