from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer
from .models import Item

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
