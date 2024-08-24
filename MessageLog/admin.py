from django.contrib import admin
from .models import ML

@admin.register(ML)
class MLAdmin(admin.ModelAdmin):
    list_display = ['ml_id', 'N_id', 'group_ID', 'sent_at', 'delivery_status', 'response_status']
    list_filter = ['delivery_status', 'response_status']
    search_fields = ['N_id', 'group_ID']
