from django.db import models

class Pengeluaran(models.Model):
    id_pengeluaran = models.IntegerField(primary_key=True)
    deskripsi_pengeluaran = models.CharField(max_length=50, null=True)
    biaya = models.IntegerField()

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.id_pengeluaran, self.deskripsi_pengeluaran)

class Piutang(models.Model):
    id_piutang = models.IntegerField(primary_key=True)
    asal_piutang = models.CharField(max_length=20)
    deskripsi_piutang = models.CharField(max_length=50, null=True)
    jumlah_piutang = models.IntegerField()
    jatuh_tempo = models.DateTimeField()

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.id_piutang, self.asal_piutang)

class Barang(models.Model):
    id_barang = models.IntegerField(primary_key=True)
    nama_barang = models.CharField(max_length=20)
    distributor = models.CharField(max_length=30)
    deskripsi_barang = models.CharField(max_length=50)

    jumlah_barang = models.IntegerField()
    satuan = models.CharField(max_length=8)
    harga_beli = models.IntegerField()
    harga_jual = models.IntegerField()

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s %s" % (self.id_barang, self.nama_barang)


# These models below have foreign key(s)
class Pendapatan(models.Model):
    id_pendapatan = models.IntegerField(primary_key=True)
    id_barang = models.ForeignKey(Barang, on_delete=CASCADE)

    nama_barang = models.CharField(max_length=20)
    pembeli = models.CharField(max_length=30)
    jumlah_pembelian = models.IntegerField()
    deskripsi_pendapatan = models.IntegerField(max_length=50)

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_barang

class Profit(models.Model):
    id_profit = models.IntegerField(primary_key=True)
    id_pengeluaran = models.ForeignKey(Pengeluaran, on_delete=CASCADE)
    id_pendapatan = models.ForeignKey(Pendapatan, on_delete=CASCADE)
    id_piutang = models.ForeignKey(Piutang, on_delete=CASCADE)

    pengeluaran_bulanan = models.IntegerField()
    pendapatan_bulanan = models.IntegerField()
    total_profit = models.IntegerField()

    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id_profit
