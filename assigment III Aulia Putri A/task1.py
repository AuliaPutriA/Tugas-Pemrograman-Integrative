#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("======================================================")
print("== MENGHITUNG TOTAL ANGKA DARI FILE TEKS indata.txt ==")
print("======================================================")

print("File 'indata.txt' telah berhasil dibuat dengan data yang telah ditulis.")

Jumlah = 0

# Buka file indata.txt untuk dibaca
try:
    with open("indata.txt", "r") as file:
        # Baca setiap baris dalam file
        for line in file:
            # Hapus karakter spasi atau newline dari setiap baris dan ubah menjadi integer
            angka = int(line.strip())
            # Tambahkan angka ke total
            Jumlah += angka
except FileNotFoundError:
    print("File 'indata.txt' tidak ditemukan.")
except ValueError:
    print("Data dalam file 'indata.txt' tidak valid.")

# Cetak total dengan pemisah koma dan dua digit desimal
print("Jumlah Keseluruhannya Adalah : {}".format(Jumlah))
