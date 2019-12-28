from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('action/', views.action, name="action"),
    re_path(r'^htmlshotview/(?P<fname>\d+)/$', views.htmlshotview, name='htmlshotview')
]