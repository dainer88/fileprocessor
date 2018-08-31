from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'crud'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<measure_id>[0-9A-Fa-f]+)/$', views.edit, name='edit'),
    url(r'^(?P<measure_id>[0-9A-Fa-f]+)/save$', views.save, name='save'),
    url(r'^load$', views.load, name='load'),
]
