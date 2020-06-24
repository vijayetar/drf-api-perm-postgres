from rest_framework import serializers

from .models import Item

class ItemSerializer(serializers.ModelSerializer):
  class Meta:
    # excludes = []
    fields = ('item_name', 'item_purchaser', 'item_date', 'item_cost')
    model = Item
  