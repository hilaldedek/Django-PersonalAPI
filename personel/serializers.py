from rest_framework import serializers
from .models import Department,Personel

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Department
        fields='__all__'

class PersonelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Personel
        fields=('first_name','last_name','title')

class DepartmentPersonalSerializer(serializers.ModelSerializer):
    personel=PersonelSerializer(many=True,read_only=True)
    class Meta:
        model=Department
        fields=('id','name','personel')