from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    # Define fields you want to display in the admin interface
    list_display = ('title', 'color_event', 'start_date', 'end_date', 'created_at')
    # Optionally, you can define search fields
    search_fields = ('title', 'title')


admin.site.register(Event, EventAdmin)