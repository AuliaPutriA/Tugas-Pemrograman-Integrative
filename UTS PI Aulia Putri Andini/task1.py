# Nama: Aulia Putri Andini
# NIM: 239902246 (PMM)
# UTS

print("=====================================================")
print("=== PROGRAM MEMBACA BILANGAN BULAT DAN MEMBAGINYA ===")
print("=====================================================")

import math

# Membaca bilangan bulat dari pengguna
BilanganBulat = int(input("Masukkan bilangan bulat anda : "))

# Menghitung hasil pembagian
JumlahHari = 365
hasil = BilanganBulat / JumlahHari

# Mengubah hasil menjadi sebelas tempat desimal jika ada
HasilDesimal = round(hasil, 11)

# Menampilkan hasil dengan sebelas tempat desimal
print("Hasil pembagian dengan jumlah hari dalam tahun ini yaitu :", round(hasil, 11))
