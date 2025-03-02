from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserModelSerializer
items = ["Hello world"] #list  + +
# @except_csrt
@api_view(['GET', 'POST'])
def item_list(request):
    if request.method == 'GET':
        return Response({'items':items}, status=status.HTTP_200_OK)        
    if request.method == 'POST':
        items.append(request.data['item'])
        return Response({"message":"Item added successfully!", "items":items}, status=status.HTTP_201_CREATED)

# Python dictionary: JSON, Dict
@api_view(['GET','POST'])
def user_auth(request):
    if request.method == 'GET':
        try:
            users_object = User.objects.all()
            serializer_data = UserModelSerializer(users_object, many=True)
            
            return Response({'data':serializer_data.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'error': "Something went wrong"},status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        print(request.data)
        data_received = request.data
        serializer = UserModelSerializer(data = data_received)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Successfully data updated', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        