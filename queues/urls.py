from django.conf.urls import url, include
from django.contrib import admin
from queues import views

urlpatterns = [
    url(r'^queue/(?P<queue_id>\w+)/$', views.queue, name='queue')
]