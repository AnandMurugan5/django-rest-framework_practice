from dataclasses import field
from django.contrib.auth.models import User,Group
from rest_framework import serializers

class userserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        field = ['url','username','email','groups']

class groupserializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        field = ['url','username']
