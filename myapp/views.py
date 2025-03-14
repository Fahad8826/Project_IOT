
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from myapp.models import Users
from rest_framework import generics,status
from .serializers import UserSerializers,AbstractUserSerializers


# Create your views here.

# ------------------CRUD operation of user creation---------------
class UserCreate(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class UserReadUpdate(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers

class UserDelete(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializers


# ---------------------Authentication-------------------------

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AbstractUserSerializers
    permission_classes = [AllowAny]

# Login View using DRF's built-in TokenObtainPairView
class LoginView(TokenObtainPairView):
    permission_classes = [AllowAny]