# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError

from maintenancemode.utils import set_maintenance_mode


class Command(BaseCommand):
    help = 'Turn on / turn off maintenance mode state.'

    def add_arguments(self, parser):
        parser.add_argument('mode', nargs='?', help='<on|off>')

    def handle(self, *args, **options):
        mode = options.get('mode', args[0] if len(args) > 0 else None)
        if mode is not None:
            if mode.lower() in ['on', 'yes', 'true', '1']:
                set_maintenance_mode(True)
                return
                
            elif mode.lower() in ['off', 'no', 'false', '0']:
                set_maintenance_mode(False)
                return

        raise CommandError("Usage is maintenance <on|off>")
