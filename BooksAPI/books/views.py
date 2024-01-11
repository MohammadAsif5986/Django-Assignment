from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import generics
from .serializers import UserSerializer,BookSerializers
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Book

# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse('Hello, Django!')

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (IsAuthenticated, )

class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    permission_classes = (IsAuthenticated, )