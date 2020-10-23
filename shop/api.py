from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from .serializers import ItemSerializer, OrderSerializer, OrderItemSerializer
from .models import Item, Order, OrderItem
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def item_detail(request,item_id):
    item = Item.objects.get(pk=item_id)
    serializer = ItemSerializer(item,many=False)

    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_cart(request, item_id):
    # get item to add
    item = get_object_or_404(Item, pk=item_id)
    # create the the order then add the item
    print(item.id)
    order_item, create = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    # check if user has active order
    order_query_set = Order.objects.filter(user=request.user, ordered=False)
    if order_query_set.exists():
        order = order_query_set[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()

            return Response({"message": "quantity successfully updated"})
        else:
            order.items.add(order_item)
            return Response({"message": "item successfully added"})
    else:
        order = Order.objects.create(user=request.user, order_date=timezone.now())
        order.items.add(order_item)
        return Response({"message": "quantity successfully updated"})

@api_view(['DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_from_cart(request, item_id):
    # get item to add
    item = get_object_or_404(Item, pk=item_id)
    # get users order
    order_query_set = Order.objects.filter(user=request.user, ordered=False)
    # check if order exists
    if order_query_set.exists():
        order = order_query_set[0]
        # check if item exists in the order
        if order.items.filter(item__pk=item_id).exists():
            order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
            # remove item
            order.items.remove(order_item)
            return Response({"Message":"the item was removed from the order"})
        else:
            return Response({"Message":"the item was not in the order"})
    else:
        return Response({"Message":"No active order"})

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_cart_items(request):
    order = Order.objects.get(user=request.user, ordered=False)
    items = order.items.all()
    serializer = OrderItemSerializer(items, many=True)

    return Response(serializer.data)





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        

