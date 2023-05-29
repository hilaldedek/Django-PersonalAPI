from django.shortcuts import render
from .serializers import DepartmentSerializer, PersonelSerializer,DepartmentPersonalSerializer
from .models import Department, Personel
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView ,ListAPIView


class DepartmentListCreateView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class PersonelListCreateView(ListCreateAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer


class PersonelRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Personel.objects.all()
    serializer_class = PersonelSerializer

class DepartmentPersonelView(ListAPIView):
    queryset=Department.objects.all()
    serializer_class=DepartmentPersonalSerializer

    def get_queryset(self):
            """
            Optionally restricts the returned purchases to a given user,
            by filtering against a `department` query parameter in the URL.
            """
            department = self.kwargs['department']
            if department is not None:
                return Department.objects.filter(name__iexact=department)
        