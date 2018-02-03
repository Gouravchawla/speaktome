from django.http import HttpResponse
from django.shortcuts import render

from .models import Event, Question, Option


def events_list(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events_list.html', context)