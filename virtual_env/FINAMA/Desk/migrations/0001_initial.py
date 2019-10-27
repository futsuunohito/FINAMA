# Generated by Django 2.2 on 2019-10-27 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id_barang', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_barang', models.CharField(max_length=20)),
                ('distributor', models.CharField(max_length=30)),
                ('deskripsi_barang', models.CharField(max_length=50)),
                ('jumlah_barang', models.IntegerField()),
                ('satuan', models.CharField(max_length=8)),
                ('harga_beli', models.IntegerField()),
                ('harga_jual', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pendapatan',
            fields=[
                ('id_pendapatan', models.IntegerField(primary_key=True, serialize=False)),
                ('nama_barang', models.CharField(max_length=20)),
                ('pembeli', models.CharField(max_length=30)),
                ('jumlah_pembelian', models.IntegerField()),
                ('deskripsi_pendapatan', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('id_barang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Desk.Barang')),
            ],
        ),
        migrations.CreateModel(
            name='Pengeluaran',
            fields=[
                ('id_pengeluaran', models.IntegerField(primary_key=True, serialize=False)),
                ('deskripsi_pengeluaran', models.CharField(max_length=50, null=True)),
                ('biaya', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Piutang',
            fields=[
                ('id_piutang', models.IntegerField(primary_key=True, serialize=False)),
                ('asal_piutang', models.CharField(max_length=20)),
                ('deskripsi_piutang', models.CharField(max_length=50, null=True)),
                ('jumlah_piutang', models.IntegerField()),
                ('jatuh_tempo', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profit',
            fields=[
                ('id_profit', models.IntegerField(primary_key=True, serialize=False)),
                ('pengeluaran_bulanan', models.IntegerField()),
                ('pendapatan_bulanan', models.IntegerField()),
                ('total_profit', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('id_pendapatan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Desk.Pendapatan')),
                ('id_pengeluaran', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Desk.Pengeluaran')),
                ('id_piutang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Desk.Piutang')),
            ],
        ),
    ]
