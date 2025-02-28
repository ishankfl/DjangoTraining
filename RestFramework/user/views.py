from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

items = ["Hello world"] #list  + +
@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        return Response({'items':items}, status=status.HTTP_200_OK)
        
    if request.method == 'POST':
        items.append(request.data['item'])
        return Response({"message":"Item added successfully!", "items":items}, status=status.HTTP_201_CREATED)

# Python dictionary: JSON