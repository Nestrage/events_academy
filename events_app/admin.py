from django.contrib import admin

# Register your models here.
from events_app.models import Event, Guest

admin.site.register(Event)
admin.site.register(Guest)