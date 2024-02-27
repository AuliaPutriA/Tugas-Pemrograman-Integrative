#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("====================================================")
print("== MENGHITUNG TOTAL ANGKA HINGGA -1 AKAN BERHENTI ==")
print("====================================================")

Jumlah = 0

while True:
    angka = input("Masukkan Angka Sampai Dengan -1 : ")

    if angka == "-1":
        break

    if angka.isdigit():
        angka = int(angka)
        Jumlah += angka
    else:
        print("Input harus berupa angka")

print("Jumlah Keseluruhannya Adalah : ", Jumlah)