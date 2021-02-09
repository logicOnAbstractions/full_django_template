from django.urls import path
from uploader.views import image_upload, UploadFileView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'uploader'
urlpatterns = [
    path('', image_upload, name='upload'),
    path('class', UploadFileView.as_view(), name='upload_cls'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)