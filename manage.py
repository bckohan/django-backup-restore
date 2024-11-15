#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
import typing as t
from pathlib import Path


def main(settings: t.Optional[str] = None):
    """Run administrative tasks."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", settings or "tests.settings.default"
    )
    try:
        import django
        from django.core.management import execute_from_command_line

        # poetry can't handle a namespace package that belongs in a namespace of an installed dependency
        # we solve this by making sure symlinks exist in our virtual environment. Not an issue when the
        # wheels are installed via pip. TODO - consider opening an issue on poetry because this should
        # work

        backup = Path(__file__).parent / "django/backup"
        restore = Path(__file__).parent / "django/restore"

        venv_backup = Path(django.__file__).parent / "backup"
        venv_restore = Path(django.__file__).parent / "restore"

        if not venv_backup.exists():
            os.symlink(backup, venv_backup)

        if not venv_restore.exists():
            os.symlink(restore, venv_restore)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
