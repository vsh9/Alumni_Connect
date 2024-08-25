from django.contrib import admin

from .models import Notification

@admin.register(Notification)
class NTFAdmin(admin.ModelAdmin):
    list_display = ['n_id', 'event_id', 'n_type', 'n_content', 'priority']
    list_filter = ['n_type', 'event_id', 'priority']
    search_fields = ['n_id', 'event_id']

