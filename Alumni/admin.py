from django.contrib import admin
from .models import Alumni

@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('Alumni_ID', 'First_Name', 'Last_Name', 'Email', 'Graduation_Year', 'Degree', 'Major', 'Occupation')
    search_fields = ('First_Name', 'Last_Name', 'Email', 'Graduation_Year', 'Degree', 'Major', 'Occupation')
    list_filter = ('Graduation_Year', 'Degree', 'Major')
