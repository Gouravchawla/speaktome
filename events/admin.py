from django.contrib import admin

from .models import Event, Question, Option


admin.site.register(Event)
admin.site.register(Question)
admin.site.register(Option)