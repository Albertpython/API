from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AutoSerializer
from .models import Auto


class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all().order_by('name')
    serializer_class = AutoSerializer

