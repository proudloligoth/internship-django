from django.conf.urls import patterns, include, url
from . import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testDjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.ProductListView.as_view(), name="list"),
    url(r'^(?P<pk>[0-9]+/$)', views.ProductDetailView.as_view(), name="detail"),
)
