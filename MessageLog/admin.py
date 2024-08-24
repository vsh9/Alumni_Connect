from django.contrib import admin
from .models import ML

@admin.register(ML)
class MLAdmin(admin.ModelAdmin):
    list_display = ['ml_id', 'n_id', 'sent_at', 'delivery_status', 'response_status']
    list_filter = ['delivery_status', 'response_status']
    search_fields = ['n_id']
