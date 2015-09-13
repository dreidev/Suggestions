from django.conf.urls import patterns, url
from test_app.views import DummyDetailView, SecondDummyDetailView

urlpatterns = patterns(
    '',
    url(
        r'^dummy/(?P<pk>[0-9]+)/$',
        DummyDetailView.as_view(), name='dummy-detail'),
    url(
        r'^dummy2/(?P<pk>[0-9]+)/$',
        SecondDummyDetailView.as_view(), name='dummy2-detail'),
    )
