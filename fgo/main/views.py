from django.shortcuts import render
from .models import Servant
from rest_framework import generics
from .serializers import ServantSerializer


class ServantListView(generics.ListAPIView):
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer


class ServantDetailView(generics.RetrieveAPIView):
    queryset = Servant.objects.all()
    serializer_class = ServantSerializer

