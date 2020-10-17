from django.shortcuts import render
from rest_framework import generics
from .serializers import SalesSerializer
from .models import Sales
from .permissions import IsAuthorOrReadOnly


# Create your views here.


class SalesList(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class SalesDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
