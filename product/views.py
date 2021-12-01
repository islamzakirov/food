from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.authentication import BaseAuthentication
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

class FoodViewSet(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filterset_field = ['name', 'content']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'price']
    ordering = ['name']
    search_fields = ['name']
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FoodNumberPaginations(PageNumberPagination):
    page_size = 3

class AloqaViewSet(viewsets.ModelViewSet):
    queryset = Aloqa.objects.all()
    serializer_class = AloqaSerializer
    filterset_field = ['name', 'number']
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name', 'number']
    ordering = ['name']
    search_fields = ['name']
