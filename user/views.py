from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .models import User
from .serializers import UserCreateSerializer


# Create your views here.

class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

