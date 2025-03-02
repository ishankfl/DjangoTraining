from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserModelSerializer
from rest_framework import viewsets
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
        
class UserViewSet(viewsets.ViewSet):
    # if request.method == 'GET':
    def __init__(self, **kwargs):
        # self.name = kwargs['hello']
        super().__init__(**kwargs)
        
    def list(self, request): #autmatically  called get
        user_obj = User.objects.all()
        serrializers = UserModelSerializer(user_obj, many = True)
        return Response({'data':serrializers.data}, status=status.HTTP_200_OK)
    
    def create(hello,request):
        hello.name 
        serializer = UserModelSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data}, status=status.HTTP_201_CREATED)  
    

class UserModelViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all()
    serializer_class = UserModelSerializer
    
    def get_queryset(self):
        queryset = User.objects.all()
        
        username_fromcustomer = self.request.query_params.get('username',None)
        # username_fromcustomer = 'kafle'
        if username_fromcustomer: # if username is not None
            queryset = queryset.filter(username = username_fromcustomer)
        return queryset
        # return super().get_queryset()
    

class Something:
    def __init__(self, name):
        self.name = name
    def data_retrive (self):
        self.name

# M = 
# V
# T