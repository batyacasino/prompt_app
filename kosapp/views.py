from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Client
from django.views.generic import View

from .forms import ClientForm


def index(request):
	clients = Client.objects.all()
	return render(request, 'kosapp/index.html', {"clients": clients,})

class AddClient(View):
	def get(self, request):
		form = ClientForm()
		return render(request, 'kosapp/add_client.html', {"form": form})

	def post(self, request):
		bound_form = ClientForm(request.POST)
		if bound_form.is_valid():
			new_client = bound_form.save()
			return render(request, 'kosapp/detail_client.html', {"client": new_client,})			
		return render(request, 'kosapp/add_client.html', {"form": bound_form})

def detail_client(request, pk):
	client = Client.objects.get(id=pk)
	return render(request, 'kosapp/detail_client.html', {
													"client": client,
												})

class ClientUpdate(View):
	def get(self, request, pk):
		client = Client.objects.get(id=pk)
		bound_form = ClientForm(instance=client)
		return render(request, 'kosapp/client_update_form.html', {"form": bound_form, 'client': client})

class ClientDelete(View):
	def get(self, request, pk):
		client = Client.objects.get(id=pk)
		return render(request, 'kosapp/client_delete_form.html', {'client': client})

		def post(self, request, pk):
			client = Client.objects.get(id=pk)
			client.delete()
			clients = Client.objects.all()
			return render(request, 'kosapp/index.html', {"clients": clients,})

def alldelete(request):
	clients = Client.objects.all()
	clients.delete()
	return render(request, 'kosapp/index.html', {"clients": clients,})