from django.conf.urls import patterns, url, handler404

from api import views

urlpatterns = patterns('',
    url(r'^reset_placements', views.reset_placements, name='reset_placements'),

    url(r'^verify_login', views.verify_login, name='verify_login'),

    url(r'^course/(?P<course_id>[a-zA-Z0-9\-]{36})/email', views.email_class, name='email_class'),

    url(r'^students/lookup', views.find_student_by_name, name='find_student_by_name'),
    url(r'^students/incomplete', views.list_incomplete_students, name='list_incomplete_students'),
    url(r'^students', views.list_students, name='list_students'),

    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/ignore/true', views.ignore_student, name='ignore_student'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/ignore/false', views.stop_ignore_student, name='stop_ignore_student'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/ignore', views.is_ignored, name='is_ignored'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/reset/placements', views.reset_student_placements, name='reset_student_placements'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/reset/requests', views.reset_student_requests, name='reset_student_requests'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/request/(?P<course_id>[a-zA-Z0-9\-]{36})', views.add_student_request, name='add_student_request'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/enroll/(?P<course_id>[a-zA-Z0-9\-]{36})', views.add_student_placement, name='add_student_placement'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})/unenroll/(?P<course_id>[a-zA-Z0-9\-]{36})', views.remove_student_placement, name='remove_student_placement'),
    url(r'^student/(?P<student_id>[a-zA-Z0-9\-]{36})', views.load_student, name='load_student'),
    url(r'^student/pub/(?P<student_id>[a-zA-Z0-9\-]{36})', views.pub_load_student, name='pub_load_student'),

    url(r'', views.handler404, name='handler404')
)
