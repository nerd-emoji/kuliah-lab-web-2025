from django.urls import path
from . import views

urlpatterns = [
    path("", views.mahasiswa_list, name="mahasiswa_list"),
]