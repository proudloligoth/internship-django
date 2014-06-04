from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# /home
# /accounts
#     /profile
#     /login
#     /logout
#     /register
#     /orders/$oid
#     /orderhistory
# /browse
# 	/search/$keyword
# /products/$pid
# /checkout
# /payment
# /contact

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('products.urls')),
    url(r'^product/', include('products.urls')),

    url(r'^cart/', 'testDjango.views.cart'),
    url(r'^contact/', 'testDjango.views.contact'),
    url(r'^checkout/', 'testDjango.views.checkout'),
    url(r'^payment/', 'testDjango.views.payment'),

    url(r'^accounts/', include('accounts.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
