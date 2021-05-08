
from django.contrib import admin
from django.urls import path,include
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from wien.urls import router as wien_router
from wien.views import upload as wien_upload,download as wien_download


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(wien_router.urls)),
    path('upload/<str:newpreset_name>',wien_upload),
    path('download/<str:preset_name>/',wien_download),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
