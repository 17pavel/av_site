from unicodedata import category
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from rest_framework import generics, permissions
from .serializers import *
from .models import *


class CarList(generics.ListCreateAPIView):
    # queryset = Products.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user = self.request.user        
        return Products.objects.filter(category="cars")

class MotoList(generics.ListCreateAPIView):
    # queryset = Products.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user = self.request.user        
        return Products.objects.filter(category="moto")

class TruckList(generics.ListCreateAPIView):
    # queryset = Products.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user = self.request.user        
        return Products.objects.filter(category="truck")

class SpecList(generics.ListCreateAPIView):
    # queryset = Products.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user = self.request.user        
        return Products.objects.filter(category="spec")

class ItemList(generics.ListCreateAPIView):
    
    serializer_class = ItemsSerializer
    permission_classes = [permissions.AllowAny]
    
    def get_queryset(self):
        user = self.request.user        
        return Products.objects.all()

class ItemRetrive(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.AllowAny]

class ImageRetrive(generics.RetrieveAPIView):
    queryset = Images.objects.all()
    serializer_class = ItemsSerializer
    permission_classes = [permissions.AllowAny]

class CategoryList(generics.ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


class ItemCreate(generics.ListCreateAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and # queryset.
    # We specify TodoSerializer which we have earlier implemented
    serializer_class = ItemsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user        
        return Products.objects.filter(user=user).order_by('-created')
    
    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(user=self.request.user)

class ItemRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ItemsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return Todo.objects.filter(user=user)


class TodoListCreate(generics.ListCreateAPIView):
    # ListAPIView requires two mandatory attributes, serializer_class and # queryset.
    # We specify TodoSerializer which we have earlier implemented
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]
    # queryset = Todo.objects.all()
    def get_queryset(self):
        user = self.request.user        
        return Todo.objects.filter(user=user).order_by('-created')
    
    def perform_create(self, serializer):
        #serializer holds a django model
        serializer.save(user=self.request.user) 

class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return Todo.objects.filter(user=user)

class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self,serializer):
        serializer.instance.completed=not(serializer.instance.completed)
        serializer.save()

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request) # data is a dictionary
            user = User.objects.create_user(
                username=data['username'], 
                password=data['password'])
            user.save()

            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201) 
        except IntegrityError:
            return JsonResponse(
                {'error':'username taken. choose another username'}, 
                status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password'])
        if user is None:
            return JsonResponse(
                {'error':'unable to login. check username and password'},
                status=400)
        else: # return user token
            try:
                token = Token.objects.get(user=user)
            except: # if token not in db, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
