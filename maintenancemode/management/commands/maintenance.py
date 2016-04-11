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
            try:
                maintenance_duration = int(command)
            except ValueError:
                maintenance_duration = None
            if maintenance_duration:
                maintenance.activate(maintenance_duration)
                if verbosity > 0:
                    self.stdout.write(
                        "Maintenance mode was activated "
                        "succesfully for %s seconds" % maintenance_duration
                    )
                return
            elif command.lower() in ('on', 'activate'):
                maintenance.activate()
                if verbosity > 0:
                    self.stdout.write(
                        "Maintenance mode was activated succesfully")
                return
            elif command.lower() in ('off', 'deactivate'):
                maintenance.deactivate()
                if verbosity > 0:
                    self.stdout.write(
                        "Maintenance mode was deactivated succesfully")
                return

        if command not in self.opts:
            raise CommandError(
                "Allowed commands are: %s or maintenance duration in seconds"
                % '|'.join(self.opts)
            )
