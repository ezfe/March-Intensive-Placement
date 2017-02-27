from django.contrib import admin
from People.models import Student
from django import forms

# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'grade', 'ford_sayre', 'hartford_tech', 'should_ignore', 'no_participate_previous', 'student_leader', 'common_ground', 'notes', 'email']
    list_display = ['full_name', 'grade', 'ford_sayre', 'hartford_tech', 'should_ignore', 'has_course', 'has_requests', 'no_participate_previous']
    list_filter = ['grade', 'ford_sayre', 'hartford_tech', 'should_ignore', 'no_participate_previous']
    search_fields = ['first_name', 'last_name']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(StudentAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'notes':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield

    def make_ignored(modeladmin, request, queryset):
        queryset.update(should_ignore=True)
    make_ignored.short_description = "Ignore student(s)"

    def reverse_make_ignored(modeladmin, request, queryset):
        queryset.update(should_ignore=False)
    reverse_make_ignored.short_description = "Un-ignore student(s)"

    def mark_np(modeladmin, request, queryset):
        queryset.update(no_participate_previous=True)
    mark_np.short_description = "Mark Non-Participate"

    def mark_p(modeladmin, request, queryset):
        queryset.update(no_participate_previous=False)
    mark_p.short_description = "Mark Participate"

    actions = [make_ignored, reverse_make_ignored, mark_p, mark_np]


admin.site.register(Student, StudentAdmin)
