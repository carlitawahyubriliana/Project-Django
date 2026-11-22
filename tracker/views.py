from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Tugas
from .services import sort_tasks


@login_required
def daftar_tugas(request):

    # Ambil waktu sekarang
    now = timezone.now()

    # Ambil seluruh tugas milik user yang login
    tasks = Tugas.objects.filter(
        mata_kuliah__user=request.user
    ).select_related("mata_kuliah")

    # Ubah queryset menjadi list
    tasks = list(tasks)

    # Klasifikasi dan urutkan
    tasks = sort_tasks(tasks, now)

    return render(
        request,
        "tracker/daftar_tugas.html",
        {
            "tasks": tasks
        }
    )