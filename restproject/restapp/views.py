from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets,permissions
from restproject.restapp.serializers import userserializers,groupserializers
# Create your views here.
class userviewset(viewsets.ModelViewSet):
    queryset = User.objects.order_by('-date_joined')
    serializer_class = userserializers
    permissions_classes = [permissions.IsAuthenticated]

class gruopviewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = groupserializers
    permissions_classes =  [permissions.IsAuthenticated]