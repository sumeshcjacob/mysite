from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'signups.views.home', name='home'),
    url(r'^thank-you/$', 'signups.views.thankyou', name='thankyou'),
    url(r'^about/$', 'signups.views.about', name= 'about'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                         document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                           document_root = settings.MEDIA_ROOT)
    
