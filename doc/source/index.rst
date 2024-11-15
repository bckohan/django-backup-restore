.. include:: ./refs.rst
.. role:: big

=====================
Django Backup Restore
=====================

A generic, pluggable backup and restore command framework for Django_.

**django-backup-restore makes it easy to:**

    * Backup all database and python context state of your Django website and restore from specific
      timepoints.
    * Plugin custom state to the backup/restore process.
    * Use a common CLI interface to backup/restore all your Django projects.
    * Pull production state into development.


:big:`Installation`

1. Clone django-typer from GitHub_ or install a release off PyPI_ :

    .. code:: bash

        pip install django-backup-restore

    rich_ is a powerful library for rich text and beautiful formatting in the terminal.
    It is not required, but highly recommended for the best experience:

    .. code:: bash

        pip install "django-backup-restore[rich]"

2. Add ``django.backup`` and/or ``django.restore`` to your ``INSTALLED_APPS`` setting:

    .. code:: python

        INSTALLED_APPS = [
            ...
            'django.restore',
            'django.backup',
        ]

    .. tip::

        The backup and restore commands are in separate applications because you may want to
        disable either command for specific deployments. For example, to protect your production
        environment from accidental restores it is a good idea to not include the 
        ``django.restore`` app in the stack.

3. Optionally add ``django_typer`` to your ``INSTALLED_APPS`` setting:

    .. code:: python

        INSTALLED_APPS = [
            ...
            'django_typer',
        ]

   *You only need to install django_typer as an app if you want to use the shellcompletion command
   to enable tab-completion or if you would like django-typer to install*
   :ref:`rich traceback rendering <configure-rich-exception-tracebacks>` *for you - which it does
   by default if rich is also installed.*


:big:`Basic Example`

|

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   tutorial
   howto
   reference
   changelog
