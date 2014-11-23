from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from .views import Data, TimeLine

urlpatterns = patterns(
    '',

    # pylint: disable=E1101
    #         Instance of <class> has no <member>
    url(r'^$', RedirectView.as_view(url='timeline')),
    url(r'^timeline/$', TimeLine.as_view(), name='timeline'),
    url(r'^data.?j?s?/?$', Data.as_view(), name='data.js')
)
