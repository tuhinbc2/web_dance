from django.conf.urls import patterns, include, url

from django.contrib import admin
import tuhinview
import firstpage
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'helloapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ctime/$', tuhinview.current_datetime),
    url(r'^ptime/plus/(\d{1,2})/$', tuhinview.hours_ahead),
    url(r'^sum/(\d+)/(\d+)$', tuhinview.sum),
    url(r'^firstpage/$', firstpage.handleFirstPage),
    url(r'^page2/$', firstpage.handleSecondPage),
    #url(r'^admin/', include(admin.site.urls)),
)
