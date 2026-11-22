from django.conf import settings
from django.db import models


class MataKuliah(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="mata_kuliah"
    )

    name = models.CharField(max_length=150)
    kode = models.CharField(max_length=30)
    dosen = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.kode} - {self.name}"


class Tugas(models.Model):

    STATUS_CHOICES = [
        ("belum", "Belum"),
        ("selesai", "Selesai"),
    ]

    mata_kuliah = models.ForeignKey(
        MataKuliah,
        on_delete=models.CASCADE,
        related_name="tugas"
    )

    judul = models.CharField(max_length=200)
    deskripsi = models.TextField(blank=True)
    deadline = models.DateTimeField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="belum"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul