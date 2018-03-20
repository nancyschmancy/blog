from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^posts/', views.post_list, name='post_list'),
    url(r'^$', TemplateView.as_view(template_name='blog/index.html')),
]