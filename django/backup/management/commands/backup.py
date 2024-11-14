from django_typer.management import TyperCommand


class Command(TyperCommand):

    help = "Backup a snapshot of the current site."

    def handle(self):
        pass


