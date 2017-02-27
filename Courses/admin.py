from django.contrib import admin
from Courses.models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    fields = ['display_name', 'course_type', 'is_travel', 'max_students', 'cost', 'manual_placement', 'room']
    list_display = ['display_name', 'course_type', 'max_students', 'enrolled_students_count', 'is_travel', 'manual_placement']
    list_filter = ['course_type', 'is_travel', 'manual_placement']
    search_fields = ['display_name']

    def set_travel(modeladmin, request, queryset):
        queryset.update(is_travel=True)
    set_travel.short_description = "Mark this course as travel"

    def set_not_travel(modeladmin, request, queryset):
        queryset.update(is_travel=False)
    set_not_travel.short_description = "Mark this course as non-travel"

    def set_am(modeladmin, request, queryset):
        queryset.update(course_type='AM')
    set_am.short_description = "Mark this course as Morning/AM"

    def set_pm(modeladmin, request, queryset):
        queryset.update(course_type='PM')
    set_pm.short_description = "Mark this course as Afternoon/PM"

    def set_full_day(modeladmin, request, queryset):
        queryset.update(course_type='FULL')
    set_full_day.short_description = "Mark this course as Full Day"

    actions = [set_travel, set_not_travel, set_am, set_pm, set_full_day]


admin.site.register(Course, CourseAdmin)
