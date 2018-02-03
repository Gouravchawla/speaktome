from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Event, Poll, Question, Option


def index(request):
    return HttpResponseRedirect(reverse('events:events_list'))


def events_list(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'events/events_list.html', context)


def polls_list(request, event_id):
    polls = Poll.objects.filter(event_id=event_id)
    context = {
        'polls': polls
    }
    return render(request, 'events/polls_list.html', context)


def poll_details(request, event_id, poll_id):
    poll = get_object_or_404(
        Poll,
        id=poll_id,
        event_id=event_id
    )
    questions = Question.objects.filter(poll=poll.id)

    context = {
        'questions': questions
    }
    return render(request, 'events/poll_details.html', context)


def poll_results(request, event_id, poll_id):
    poll_queryset = get_object_or_404(
        Poll,
        id=poll_id,
        event_id=event_id
    )
    context = {}
    return render(request, 'events/events_list.html', context)