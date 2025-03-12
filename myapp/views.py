from django.shortcuts import render
from myapp.models import Users
from rest_framework import generics
from .serializers import UserSerializers


# Create your views here.


class UserCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class UserReadUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class UserDelete(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers
