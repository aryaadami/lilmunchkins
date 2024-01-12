from django.urls import path, re_path
from django.conf.urls import handler404
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.landing_page, name='landing-page'),
    path('home', views.home_page, name='home-page'),
    path('memory/<slug:slug>', views.memory_detail, name='memory-detail'),
    re_path(r'^media/(?P<path>.*)$', views.serve_media),
]


handler404 = views.custom_404
