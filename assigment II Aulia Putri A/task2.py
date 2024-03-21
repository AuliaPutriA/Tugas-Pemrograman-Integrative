#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("====================================================")
print("== MENGHITUNG TOTAL ANGKA HINGGA -1 AKAN BERHENTI ==")
print("====================================================")

Jumlah = 0

while True:
    angka = input("Masukkan Angka (-1 untuk berhenti) : ")

    if angka == "-1":
        break

    try:
        angka = float(angka)
        Jumlah += angka
    except ValueError:
        print("Input harus berupa angka")

print("Jumlah Keseluruhannya Adalah : {:.2f}".format(Jumlah))
