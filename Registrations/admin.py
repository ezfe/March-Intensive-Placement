from django.contrib import admin
from Registrations.models import Request, Placement

# Register your models here.


class RequestAdmin(admin.ModelAdmin):
    fields = ['student', 'course', 'request_rank']
    list_display = ['student', 'course', 'request_rank']
    list_filter = ['course','request_rank']
    search_fields = ['student__first_name','student__last_name','course__display_name']

class PlacementAdmin(admin.ModelAdmin):
    fields = ['student', 'course', 'leader']
    list_display = ['student', 'course']
    list_filter = ['course']
    search_fields = ['student__first_name','student__last_name','course__display_name']

admin.site.register(Request, RequestAdmin)
admin.site.register(Placement, PlacementAdmin)
