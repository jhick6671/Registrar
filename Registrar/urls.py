from django.conf.urls import patterns, include, url
from django.contrib import admin

api_patterns = patterns('',
    url(r'^', include('apps.students.api_urls'), name='students_api'),
)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'students/', include('apps.students.urls', namespace='students')),
    url(r'api/v1/', include(api_patterns, namespace='api')),
)
