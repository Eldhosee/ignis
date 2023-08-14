from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User,Events,Likes
from .serializer import UserSerializer,NewUserSerializer,EventsSerializer,LikedSerializer

@api_view(['GET']) 
def login(request):
    if request.method == 'GET':
        try:
            email = request.GET.get('email')
            password = request.GET.get('password')
            print(email,password)
            
           
            email = request.GET.get('email')
            password = request.GET.get('password')
            
            user = User.objects.get(email=email ,password=password)
            if user:
                user_pk = user.id
                return Response({'id':f'{user_pk}'})
            
            
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            

@api_view(['POST'])
def signup(request):
    if request.method=='POST':
        try:
            serializer = NewUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)
        except Exception as e:
            return Response({'error': 'Something went wrong'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET']) 
def getevents(request):
    if request.method == 'GET':
            events = Events.objects.all()
            serializer = EventsSerializer(events, many=True) 
            return Response(serializer.data)
            
@api_view(['POST']) 
def events(request):
    if request.method == 'POST':
            try:
                print(request.data)
                serializer = EventsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                     print(serializer.errors)

            except:
                 
                 return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
                 
            
        
            
@api_view(['POST']) 
def liked(request):
    if request.method == 'POST':
            try:
                print(request.data)
                serializer = LikedSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                else:
                     print(serializer.errors)

            except:
                 
                 return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
                 
@api_view(['GET']) 
def getliked(request):
    if request.method == 'GET':
            user= user = request.query_params.get('user')
            likes=Likes.objects.filter(user=user)
            for i in likes:
                 print(i)
            serializer = LikedSerializer(likes, many=True) 
            return Response(serializer.data)         
@api_view(['GET']) 
def getlikedevents(request):
    if request.method == 'GET':
            user= user = request.query_params.get('user')
            likes=Likes.objects.filter(user=user)
   
            serializer = EventsSerializer(likes, many=True) 
            return Response(serializer.data) 
    
@api_view(['DELETE'])
def delete_like(request, event_id):
    if request.method == 'DELETE':
        user = request.query_params.get('user')
        
        try:
            likes = Likes.objects.filter(user=user, likes=event_id)
            if likes.exists():
                for like in likes:
                    like.delete()
            return Response({'message': 'Like deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Likes.DoesNotExist:
            return Response({'error': 'Like not found'}, status=status.HTTP_404_NOT_FOUND)