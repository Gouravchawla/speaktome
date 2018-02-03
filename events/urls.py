from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.events_list, name='events_list'),
    url(
        r'^(?P<event_id>[0-9]+)/polls$',
        views.polls_list,
        name='polls_list'
    ),
    url(
        r'^(?P<event_id>[0-9]+)/polls/(?P<poll_id>[0-9]+)/details$',
        views.poll_details,
        name='poll_details'
        ),
    url(
        r'^(?P<event_id>[0-9]+)/polls/(?P<poll_id>[0-9]+)/results',
        views.poll_results,
        name='poll_results'
        ),

]
app_name = 'events'
