from django.db import models

# Create your models here.
class Mahasiswa(models.Model):
    nama = models.CharField(max_length=50)
    nim = models.CharField(max_length=50)

    def __str__(self):
        return self.id

class Matakuliah(models.Model):
    nama = models.CharField(max_length=50)
    mahasiswa = models.ForeignKey('Mahasiswa', on_delete=models.CASCADE)

    def __str__(self):
        return self.id