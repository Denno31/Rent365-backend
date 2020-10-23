from django.urls import path

from .api import item_list,item_detail, add_to_cart, remove_from_cart, get_cart_items

urlpatterns = [
    path('api/items-list',item_list),
    path('api/item-detail/<str:item_id>',item_detail),    
    path('api/item/<str:item_id>/add_to_cart', add_to_cart),
    path('api/item/<str:item_id>/remove_from_cart', remove_from_cart),
    path('api/item/all_items', get_cart_items)
]
