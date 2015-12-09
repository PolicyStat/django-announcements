from django import forms

from announcements.models import Announcement


class AnnouncementAdminForm(forms.ModelForm):
    """
    A custom form for the admin of the Announcement model. Has an extra field
    called send_now that when checked will send out the announcement allowing
    the user to decide when that happens.
    """

    class Meta:
        model = Announcement
        exclude = ("creator", "creation_date")
