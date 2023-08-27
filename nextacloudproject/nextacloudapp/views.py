from django.shortcuts import render
from .models import Items , Brands , Store , Staff
from .serializers import ItemsSerializer , BrandsSerializer , StoreSerializer, StaffSerializer
from rest_framework import viewsets

class ItemsViewSet(viewsets.ModelViewSet):
    serializer_class = ItemsSerializer
    queryset = Items.objects.all()

class BrandsViewSet(viewsets.ModelViewSet):
    serializer_class = BrandsSerializer
    queryset = Brands.objects.all()

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

class StaffViewSet(viewsets.ModelViewSet):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()

# Create your views here.
