# Nama: Aulia Putri Andini
# NIM: 239902246 (PMM)
# UTS

import time

print("======================================================")
print("===== PROGRAM MEMBACA TANGGAL PENGUJIAN HARI INI =====")
print("======================================================")

# Membaca angka (tanggal pengujian hari ini)
angka = int(input("Masukkan angka (tanggal pengujian hari ini): "))

# Memastikan angka yang dimasukkan bukan negatif
if angka < 0:
    print("Maaf, angka yang Anda masukkan salah! Harus positif.")
else:
    # Menghitung hasil kali semua nilai dari 1 hingga angka yang diberikan
    hasil_kali = 1
    for i in range(1, angka + 1):
        hasil_kali *= i
        print(f'\rMenghitung hasil kali {i}-{angka}', end='', flush=True)
        time.sleep(0.1)  # Memberi sedikit jeda untuk efek animasi
    print("\n")

    # Menampilkan hasil kali semua nilai
    print(f"Hasil kali semua nilai dari 1 hingga {angka} adalah: {hasil_kali}")
