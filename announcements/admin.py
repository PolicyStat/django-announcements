from django.contrib import admin

from announcements.models import Announcement
from announcements.forms import AnnouncementAdminForm


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "creator", "creation_date", "members_only")
    list_filter = ("members_only",)
    form = AnnouncementAdminForm
    fieldsets = [
        (None, {
            "fields": ["title", "content", "site_wide", "members_only"],
        }),
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            # When creating a new announcement, set the creator field.
            obj.creator = request.user
        obj.save()


try:
    admin.site.register(Announcement, AnnouncementAdmin)
except admin.sites.AlreadyRegistered:
    pass
