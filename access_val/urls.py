from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

admin.site.index_template = 'admin/index.html'
admin.autodiscover()

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls, name='admin_site'),
    path('acessos/', include('acessos.urls')),
    path('login/', RedirectView.as_view(url='/admin/login/?next=/acessos/list')),
    path('', RedirectView.as_view(url='/acessos/list')),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
