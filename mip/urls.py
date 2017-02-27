from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mip.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', include('Registrations.urls')),
    url(r'^register/', include('Registrations.urls')),
    url(r'^students/', include('People.urls')),
    url(r'^admin-django/', include(admin.site.urls)),
    url(r'^admin/', include('Placement.urls')),
    url(r'^api/', include('api.urls'))
)
