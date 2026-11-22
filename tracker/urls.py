from django.urls import path
from . import views

urlpatterns = [
    path(
        "tugas/",
        views.daftar_tugas,
        name="daftar_tugas"
    ),
]