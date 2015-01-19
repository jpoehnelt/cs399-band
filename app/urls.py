from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app.views.home', name='home'),
    url(r'^members', 'app.views.members', name='members'),
    url(r'^discography', 'app.views.discography', name='discography'),
    url(r'^tour', 'app.views.tour', name='tour'),
    # url(r'^admin/', include(admin.site.urls)),
)
