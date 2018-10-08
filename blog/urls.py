from django.conf.urls import include, url
from . import views
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    path('admin/', admin.site.urls),
    # path('api/', include('mynewapp.urls')),
    re_path('.*', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
