from django.shortcuts import render
from rest_framework import generics
from women.serializers import WomenSerializer
from .models import Women



class WomenApiView(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer
