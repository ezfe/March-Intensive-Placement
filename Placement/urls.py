from django.conf.urls import patterns, url

from Placement import views

urlpatterns = patterns('',
    url(r'^$', views.configure_placement, name='configure_placement'),
    url(r'^verify/$', views.verify_missing_students, name='verify_missing_students'),
    url(r'^settings/$', views.settings, name='settings'),
    url(r'^manage_student/$', views.manage_student, name='manage_student'),
    url(r'^view/$', views.view_results, name='view_results'),
    url(r'^view/detail/(?P<course_id>[a-zA-Z0-9\-]{36})$', views.view_results_detail, name='view_results_detail'),
    url(r'^import/$', views.import_students, name='import_students'),
    url(r'^view_requests/$', views.view_requests, name='view_requests'),
    url(r'^view_no_requests/$', views.view_no_requests, name='view_no_requests'),
    # url(r'^success/$', views.register_success, name='register_success'),
    # url(r'^(?P<course_id>[a-zA-Z0-9\-]{36})/$', views.course_detail, name='course_detail'),
)
