from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', index, name='index'),
	path('add_client/', AddClient.as_view(), name='add_client_url'),
	path('detail_client/<int:pk>/', detail_client, name='detail_client_url'),
	path('detail_client/<int:pk>/upload_docs/', UploadDocs.as_view(), name='upload_docs_url'),
	path('upload/', upload, name='upload_url'),
]


if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
