from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('employees:company_structure'), permanent=True), name='homepage'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('employees.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
