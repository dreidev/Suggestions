from django.conf.urls import patterns, url
from test_app.views import DummyDetailView

urlpatterns = patterns(
    '',
    url(
        r'^dummy/(?P<pk>[0-9]+)/$',
        DummyDetailView.as_view(), name='dummy-detail'),
    )
