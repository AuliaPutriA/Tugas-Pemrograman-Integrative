#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("==============================================================")
print("=== Program Membaca Suatu Angka dan Mencetak Tanggal Angka ===")
print("==============================================================")

import datetime

def cetak_tanggal_mendatang(hari):
    tanggal_sekarang = datetime.date.today()
    tanggal_mendatang = tanggal_sekarang + datetime.timedelta(days=hari)
    print(f"Tanggal {hari} hari dari sekarang akan menjadi: {tanggal_mendatang.strftime('%A, %d %B %Y')}")

angka = int(input("Masukkan Angka : "))
cetak_tanggal_mendatang(angka)
