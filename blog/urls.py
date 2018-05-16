# Here we're importing Django's function url and all of our views from the blog application.
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index_page, name='index'),
    url(r'^about/$', views.about_page, name='about'),
]