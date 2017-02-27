from django.conf.urls import patterns, url

from Registrations import views

urlpatterns = patterns('',
    url(r'^$', views.register, name='register'),
    url(r'^success/$', views.register_success, name='register_success'),
)