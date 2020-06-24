from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from rest_framework import generics

from .models import Item
from .serializers import ItemSerializer
from .permissions import IsPurchaserOrReadOnly

# Create your views here.

class ItemList(generics.ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsPurchaserOrReadOnly,)
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

class ItemListView(ListView):
  template_name = 'item/item_list.html'
  model = Item

class ItemDetailView(DetailView):
  template_name = 'item/item_detail.html'
  model = Item

class ItemCreateView(CreateView):
  template_name = 'item/item_create.html'
  model = Item
  fields = ['item_purchaser', 'item_name', 'item_date', 'item_cost']

class ItemUpdateView(UpdateView):
  template_name = 'item/item_update.html'
  model = Item
  fields = ['item_name','item_date', 'item_cost']

class ItemDeleteView(DeleteView):
  template_name = 'item/item_delete.html'
  model = Item
  success_url = reverse_lazy('item_list')