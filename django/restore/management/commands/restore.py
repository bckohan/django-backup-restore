from django_typer.management import TyperCommand


class Command(TyperCommand):

    help = "Restore site from a backup."

    def handle(self):
        pass


