from django.shortcuts import render
from .models import Employees , Employers
from .serializers import EmployeesSeriallizer , EmployerstSeriallizer
from rest_framework import viewsets
from django.http import JsonResponse , request
from django.views import View
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
# Create your views here.

class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeesSeriallizer
    queryset = Employees.objects.all()

class EmployersViewSet(viewsets.ModelViewSet):
    serializer_class = EmployerstSeriallizer
    queryset = Employers.objects.all()


