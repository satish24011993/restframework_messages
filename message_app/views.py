from django.shortcuts import render
from .serializers import MessagesDataSerializer
from rest_framework import generics
from .models import messages_data

# Create your views here.
class MessagesCreate(generics.CreateAPIView):
    queryset = messages_data.objects.all()
    serializer_class = MessagesDataSerializer
    http_method_names = ['post']

class MessagesList(generics.ListAPIView):
    queryset = messages_data.objects.all()
    serializer_class = MessagesDataSerializer
    http_method_names = ['get']

