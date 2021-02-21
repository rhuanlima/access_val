from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    path('admin/', admin.site.urls),
    path('acessos/', include('acessos.urls')),
    path('', RedirectView.as_view(url='/acessos/')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
