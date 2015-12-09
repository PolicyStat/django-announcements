from django.test import TestCase
from django.contrib.auth.models import User

from announcements.models import Announcement


class AnnouncementTestCase(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_user(
            "brosner",
            "brosner@gmail.com",
        )

        self.a1 = Announcement.objects.create(
            title="Down for Maintenance",
            creator=self.superuser,
        )
        self.a2 = Announcement.objects.create(
            title="Down for Maintenance Again",
            creator=self.superuser,
        )
        self.a3 = Announcement.objects.create(
            title="Down for Maintenance Again And Again",
            creator=self.superuser,
            site_wide=True,
        )
        self.a4 = Announcement.objects.create(
            title="Members Need to Fill Out New Profile Info",
            creator=self.superuser,
            members_only=True,
        )
        self.a5 = Announcement.objects.create(
            title="Expected Down Time",
            creator=self.superuser,
            members_only=True,
            site_wide=True,
        )

    def test_current(self):
        # get the announcements that are publically viewable. This is the same
        # as calling as using site_wide=False, for_members=False
        self.assertEqual(
            set(Announcement.objects.current()),
            set([self.a1, self.a2, self.a3])
        )

    def test_current_site_wide(self):
        # get just the publically viewable site wide announcements
        self.assertEqual(
            set(Announcement.objects.current(site_wide=True)),
            set([self.a3]),
        )

    def test_current_for_memebers(self):
        # get the announcements that authenticated users can see.
        self.assertEqual(
            set(Announcement.objects.current(for_members=True)),
            set([self.a1, self.a2, self.a3, self.a4, self.a5]),
        )

    def test_current_for_members_and_site_wide(self):
        # get just site wide announcements that authenticated users can see.
        self.assertEqual(
            set(Announcement.objects.current(for_members=True, site_wide=True)),  # noqa
            set([self.a3, self.a5]),
        )

    def test_current_exclude(self):
        # exclude a couple of announcements from the publically viewabled
        # messages.
        self.assertEqual(
            set(Announcement.objects.current(exclude=[self.a1.pk, self.a5.pk])),  # noqa
            set([self.a2, self.a3]),
        )
