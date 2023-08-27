from rest_framework import serializers
from .models import Items , Brands , Store , Staff

class ItemsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Items
        fields = '__all__'

class BrandsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Brands
        fields = '__all__'

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
