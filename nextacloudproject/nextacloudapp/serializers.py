from rest_framework import serializers
from .models import Employees , Employers


class EmployeesSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'
    

class EmployerstSeriallizer(serializers.ModelSerializer):
    class Meta:
        model = Employers
        fields = '__all__'