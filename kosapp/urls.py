from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', index, name='index'),
	path('add_client/', AddClient.as_view(), name='add_client_url'),
	path('detail_client/<int:pk>/', detail_client, name='detail_client_url'),
]
