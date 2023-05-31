from django.urls import path
from .views import DepartmentListCreateView,DepartmentRUDView,PersonelListCreateView,PersonelRUDView,DepartmentPersonelView

urlpatterns=[
    path('departments/',DepartmentListCreateView.as_view()),
    path('departments/<int:pk>/', DepartmentRUDView.as_view()),
    path('personels/',PersonelListCreateView.as_view()),
    path('personels/<int:pk>/',PersonelRUDView.as_view()),
    path('departments/<str:department>/',DepartmentPersonelView.as_view())
]