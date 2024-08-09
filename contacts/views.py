from django.shortcuts import render
from rest_framework.generics import *
from .models import *
from .serializers import *
from rest_framework import permissions
# Create your views here.


class ContactList(ListCreateAPIView):
   serializer_class = ContactSerializer
   permission_classes =[permissions.IsAuthenticated]
   def perform_create(self, serializer):
      serializer.save(owner=self.request.user)


   def get_queryset(self):
       return Contact.objects.filter(owner=self.request.user)


class ContactdetailView(RetrieveUpdateDestroyAPIView):
   serializer_class = ContactSerializer
   permission_classes =[permissions.IsAuthenticated]
   lookup_field = "id"
   
   def get_queryset(self):
       return Contact.objects.filter(owner=self.request.user)


