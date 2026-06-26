"""
Root URL configuration for the portfolio project.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.index_title = settings.ADMIN_INDEX_TITLE

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bio.urls')),
    path('bio/', include('bio.urls')),
    path('education/', include('education.urls')),
    path('skills/', include('skills.urls')),
    path('experience/', include('experience.urls')),
    path('projects/', include('projects.urls')),
]

handler404 = 'core.views.error_404_view'
handler500 = 'core.views.error_500_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
