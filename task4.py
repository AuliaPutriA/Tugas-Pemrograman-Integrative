#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("==================================================")
print("========= PROGRAM MENGHITUNG TOTAL NILAI =========")
print("==================================================")

angka = input("Masukkan angka : ")

if angka.isdigit():
    angka = int(angka)
    jumlah = angka * (angka + 1) // 2
    print("Jumlah nilai dari 1 sampai dengan", angka, "adalah:", jumlah)
else:
    print("Input yang Anda masukkan bukan angka.")