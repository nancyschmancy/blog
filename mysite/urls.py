from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='blog/index.html')),
    url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls')),
]
