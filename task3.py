#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("==================================================")
print("==== KLASIFIKASI ANGKA : KECIL, SEDANG, BESAR ====")
print("==================================================")

angka = (input("Masukkan angka : "))

if angka.isdigit():
    angka = int(angka)

    if angka < 100:
      print("Merupakan Kategori Angka Kecil (small)")
    elif angka <= 200:
       print("Merupakan Kategori Angka Sedang (medium)")
    else:
      print("Merupakan Kategori Angka Besar (large)")
else:
    print("Input yang Anda masukkan bukan angka.")
