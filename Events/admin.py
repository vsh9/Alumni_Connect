from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_id','event_name', 'event_date', 'location', 'event_type', 'registration_deadline', 'event_status', 'feedback_available')
    search_fields = ('event_id','event_name', 'location','event_type', 'event_status')
    list_filter = ('event_id','event_type', 'event_status', 'event_date')
    ordering = ('event_id','event_date')
