from django.conf.urls import patterns, include, url
import core.views as cv

urlpatterns = patterns('',
    url(r'^$', cv.LandingView.as_view(), name="landing"),
    url(r'api/location/$', cv.LocationAPIView.as_view(), name="api_location_list"),
    url(r'api/location/(?P<pk>\d+)/detail/$', cv.LocationAPIView.as_view(), name="api_location_detail"),
    url(r'location/$', cv.LocationListView.as_view(), name="location_list"),
    url(r'location/create$', cv.LocationCreateView.as_view(), name="location_create"),
    url(r'location/(?P<pk>\d+)/detail/$', cv.LocationDetailView.as_view(), name='location_detail'),
    url(r'location/(?P<pk>\d+)/update/$', cv.LocationUpdateView.as_view(), name='location_update'),
    url(r'location/(?P<pk>\d+)/review/create/$', cv.ReviewCreateView.as_view(), name='review_create'),
    url(r'location/(?P<pk>\d+)/review/update/$', cv.ReviewUpdateView.as_view(), name='review_update'),
    url(r'search/$', cv.SearchView.as_view(), name='search_list'),
    url(r'entrance/$', cv.entrance, name='entrance'),

)


