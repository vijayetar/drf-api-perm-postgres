from django.urls import path
from .views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemList, ItemDetail
urlpatterns = [
  path("", ItemList.as_view(), name = 'item_list'),
  path("<int:pk>/", ItemDetail.as_view(), name = 'item_detail'),
  # path("new", ItemCreateView.as_view(), name= 'item_create'),
  # path('<int:pk>/edit/', ItemUpdateView.as_view(), name='item_update'),
  # path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete'),
]

