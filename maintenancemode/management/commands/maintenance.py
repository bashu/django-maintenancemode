# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from maintenancemode import utils as maintenance


class Command(BaseCommand):
    opts = ('on', 'off', 'activate', 'deactivate')

    def add_arguments(self, parser):
        parser.add_argument('command', nargs='?', help='|'.join(self.opts))

    def handle(self, *args, **options):
        command = options.get('command', args[0] if len(args) > 0 else None)
        verbosity = int(options.get('verbosity'))

        if command is not None:
            if command.lower() in ('on', 'activate'):
                maintenance.activate()
                if verbosity > 0:
                    self.stdout.write(
                        "Maintenance mode was activated succesfully")
            elif command.lower() in ('off', 'deactivate'):
                maintenance.deactivate()
                if verbosity > 0:
                    self.stdout.write(
                        "Maintenance mode was deactivated succesfully")

        if command not in self.opts:
            raise CommandError(
                "Allowed commands are: %s" % '|'.join(self.opts))
