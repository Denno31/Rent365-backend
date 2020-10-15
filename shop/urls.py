from django.urls import path

from .api import item_list,item_detail

urlpatterns = [
    path('api/items-list',item_list),
    path('api/item-detail/<str:item_id>',item_detail)
]
