try:
    from django.views.generic.list_detail import object_detail as DetailView
except ImportError:  # Django > 1.4
    from django.views.generic.detail import DetailView
try:
    from django.conf.urls.defaults import patterns, url
except ImportError:  # Django > 1.4
    from django.conf.urls import patterns, url

from announcements.models import Announcement
from announcements.views import announcement_hide, announcement_list


announcement_detail_info = {
    "queryset": Announcement.objects.all(),
}

urlpatterns = patterns(
    "",
    url(r"^(?P<object_id>\d+)/$", DetailView,
        announcement_detail_info, name="announcement_detail"),
    url(r"^(?P<object_id>\d+)/hide/$", announcement_hide,
        name="announcement_hide"),
    url(r"^$", announcement_list, name="announcement_home"),
)
