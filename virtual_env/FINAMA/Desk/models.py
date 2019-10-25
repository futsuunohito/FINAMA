from django.db import models

# Create your models here.
class Pengeluaran(models.Model):
    id_pengeluaran = models.IntegerField(primary_key=True)
    deskripsi_pengeluaran = models.CharField(max_length=150, null=True)
    biaya = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_pengeluaran

class Piutang(models.Model):
    pass

class Barang(models.Model):
    pass

# These models below have foreign key(s)
class Pendapatan(models.Model):
    pass

class Profit(models.Model):
    pass
