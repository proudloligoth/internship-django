from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# /home
# /account
# 	/orderhistory
# /browse
# 	/search/$keyword
# /product/$pid
# /order/$oid
# /checkout
# /payment
# /login
# /logout
# /register
# /contact

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('pages.urls')),
    url(r'^home/', include('pages.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
