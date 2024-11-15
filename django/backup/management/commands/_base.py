import typing as t
from pathlib import Path

from django_typer.completers import these_strings
from django_typer.management import TyperCommand, initialize
from typer import Option
from typing_extensions import Annotated

from django.conf import settings
from django.core.files.storage import default_storage, get_storage_class
from django.utils.translation import gettext_lazy as _


class BaseBackupRestoreCommand(TyperCommand):
    storage = default_storage

    @initialize()
    def init(
        self,
        storage: Annotated[
            str,
            Option(
                help=_("The storage backend to use for backups."),
                shell_complete=these_strings(
                    getattr(settings, "STORAGES", {"default": None}).keys()
                ),
            ),
        ] = "default",
        sandbox: Annotated[
            t.Optional[Path],
            Option(
                help=_("The temporary directory that will be used to build the backup.")
            ),
        ] = None,
    ):
        if storage != "default":
            self.storage = get_storage_class(storage)()
        