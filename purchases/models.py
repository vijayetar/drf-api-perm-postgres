# from django.db import models
# import datetime
# from django.contrib.auth import get_user_model
# import django.utils
# from django.urls import reverse
# # Create your models here.

# class Item(models.Model):
# 	item_name=models.CharField('Enter name of item purchased here: ',max_length=64)

#   item_description=models.TextField('Enter description here: ',max_length=64, default=None)

#   item_cost=models.IntegerField('Enter cost of item in dollars: ',default=0)

# 	item_purchaser=models.ForeignKey('Purhchaser: ', get_user_model(),on_delete=models.CASCADE)

#   item_purchase_date=models.DateField('Enter date of purchase',default=django.utils.timezone.now)

# 	def __str__(self):
# 		return f"{self.item_name} purchased by {self.item_purchaser} at {self.item_cost} on {self.item_purchase_date}"

#   #goes back to the item list once added new items
#   def get_absolute_url(self):
#     return reverse('item_list')

from django.db import models
import datetime
from django.contrib.auth import get_user_model
import django.utils
from django.urls import reverse

# Create your models here.
class Item(models.Model):
  item_purchaser = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
  item_name = models.TextField('Select name of item', max_length=10)
  item_date = models.DateField('Enter date of purchase', default=django.utils.timezone.now)
  item_cost = models.IntegerField('Enter cost', default = 0)

  def __str__(self):
    # return self.event_name
    return f"{self.item_purchaser} did {self.item_name} on {self.item_date}"
    
  # def get_absolute_url(self):
  #   return reverse('event_detail',args=[str(self.id)])
  
  def get_absolute_url(self):
    return reverse('item_list')

