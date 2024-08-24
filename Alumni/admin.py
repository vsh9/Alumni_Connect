from django.contrib import admin
from .models import alumni

@admin.register(alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('alumni_ID', 'first_name', 'last_name', 'email', 'graduation_year', 'degree', 'major', 'occupation')
    search_fields = ('first_name', 'last_name', 'email', 'graduation_year', 'degree', 'major', 'occupation')
    list_filter = ('graduation_year', 'degree', 'major')
