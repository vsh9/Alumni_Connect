from django.contrib import admin

from .models import NTF

@admin.register(NTF)
class NTFAdmin(admin.ModelAdmin):
    list_display = ['N_id', 'event_id', 'N_type', 'N_content', 'Priority']
    list_filter = ['N_type', 'event_id', 'Priority']
    search_fields = ['N_id', 'event_id']

