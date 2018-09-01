from django.conf.urls import url
from django.contrib import admin

from . import views

app_name = 'crud'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<measure_id>[0-9A-Fa-f]+)/$', views.edit, name='edit'),
    url(r'^(?P<measure_id>[0-9A-Fa-f]+)/savemeasure$', views.savemeasure, name='savemeasure'),
    url(r'^(?P<measure_id>[0-9A-Fa-f]+)/deletemeasure$', views.deletemeasure, name='deletemeasure'),
    url(r'^load$', views.load, name='load'),
    url(r'^selectbydateandtime$', views.selectbydateandtime, name='selectbydateandtime'),
]
