from django.conf.urls import patterns, include, url
from apps.students import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^main$', views.StudentView.as_view()),
    # url(r'^next$', views.NextView.as_view()),
)
