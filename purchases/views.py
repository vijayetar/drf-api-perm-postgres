from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from rest_framework import generics
from rest_framework.response import Response
from django.forms.models import model_to_dict

from .models import Item
from .serializers import ItemSerializer
from .permissions import IsPurchaserOrReadOnly

# Create your views here.

class ItemList(generics.ListCreateAPIView):
  queryset = Item.objects.all()
  serializer_class = ItemSerializer

#James playing for fun
  #create a separate method to get the template that you want to render
  # def get(self, request):
  #   queryset = Item.objects.filter(id=request.user.id)
  #   serializer = [model_to_dict(ItemSerializer(i)) for i in queryset]
  #   return Response(serializer)

  # data = self.get_queryset()
  # for item in data:
  #    item['product'] = model_to_dict(item['product'])
  # return HttpResponse(json.simplejson.dumps(data), mimetype="application/json")





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