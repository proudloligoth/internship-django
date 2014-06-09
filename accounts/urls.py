from django.conf.urls import patterns, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required

from .views import ProfileDetailView, ProfileUpdateView


admin.autodiscover()

# /home
# /accounts
# /profile
# /login
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

                       url(r'^profile/$', login_required(ProfileDetailView.as_view())),
                       url(r'^profile/edit', login_required(ProfileUpdateView.as_view())),
                       url(r'^login/', 'django.contrib.auth.views.login'),
                       url(r'^logout/', login_required('django.contrib.auth.views.logout')),
                       url(r'^register/', 'accounts.views.register'),
                       url(r'^orders/', login_required('accounts.views.orders')),
                       url(r'^orderhistory/', login_required('accounts.views.orderhistory')),
)
