from django.contrib import admin

from .models import Event, Poll, Question, Option
from .models import Event, Poll, Question, Option


admin.site.register(Event)
admin.site.register(Poll)
admin.site.register(Question)
admin.site.register(Option)