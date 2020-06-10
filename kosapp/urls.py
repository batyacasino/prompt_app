from django.urls import path
from .views import *

urlpatterns = [
	path('', index, name='index'),
	path('add_client/', AddClient.as_view(), name='add_client_url'),
	path('detail_client/<int:pk>/', detail_client, name='detail_client_url'),
	path('detail_client/<int:pk>/update/', ClientUpdate.as_view(), name='client_update_url'),
	path('detail_client/<int:pk>/delete/', ClientDelete.as_view(), name='client_delete_url'),
	path('alldelete/', alldelete, name='alldelete'),
]
