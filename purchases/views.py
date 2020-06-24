from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Item
from django.urls import reverse_lazy

# Create your views here.

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