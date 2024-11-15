import typing as t

from django_typer.management import command

from django.utils.translation import gettext_lazy as _

from ._base import BaseBackupRestoreCommand


class Command(BaseBackupRestoreCommand, chain=True):
    help = _("Backup a snapshot of the current site.")  # type: ignore

    def upload(self):
        pass

    @command(result_callback=upload)
    def stack(self):
        print("stack")
        return "stack"

    @command()
    def database(self):
        print("database")
        return "database"

    @command()
    def media(self):
        print("media")
        return "media"
