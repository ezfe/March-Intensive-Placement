from django.conf.urls import patterns, url

from People import views

urlpatterns = patterns('',
    url(r'^$', views.students, name='students'),
    url(r'^(?P<student_id>[a-zA-Z0-9\-]{36})/$', views.student_detail, name='student_detail'),
)
