from __future__ import print_function

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from announcements.models import Announcement


def str_announcement(a):
    return '%d: %s - %s' % (a.pk, a.title, a.content)


class Command(BaseCommand):
    help = 'Create, delete, or list announcements.'
    args = '[title, content]'

    def add_arguments(self, parser):
        parser.add_argument(
            '-l'
            '--list',
            dest='list',
            action='store_true',
            default=False,
            help='List current announcements.',
        ),
        parser.add_argument(
            '-d',
            '--delete',
            dest='delete',
            help='The title or pk of the announcement to delete.',
        ),

    def handle(self, *args, **options):
        # List existing announcements.
        User = get_user_model()
        if options.get('list'):
            announcements = Announcement.objects.all()
            if announcements:
                for a in announcements:
                    print(str_announcement(a))
            else:
                print('No announcements exist.')
            return

        # Delete an announcement.
        delete = options.get('delete')
        if delete:
            for field in ['pk', 'title__iexact']:
                try:

                    a = Announcement.objects.get(**{field: delete})
                    s = str_announcement(a)
                    a.delete()
                    print('Deleted announcement:')
                    print(s)
                    return
                except (ValueError, Announcement.DoesNotExist):
                    pass
            raise CommandError(
                'The announcement with title or PK "%s" does not exist.' % delete,  # noqa
            )

        # Create an announcement.
        try:
            title, content = args
        except ValueError:
            raise CommandError(
                'To create an announcement, you must specify the title and content.',  # noqa
            )
        try:
            admin = User.objects.filter(is_superuser=True)[0]
        except IndexError:
            raise CommandError(
                'Please create a superuser account in order to make announcements.',  # noqa
            )

        a = Announcement.objects.create(
            title=title,
            content=content,
            creator=admin,
            site_wide=True,
        )
        print('Created announcement:')
        print(str_announcement(a))
