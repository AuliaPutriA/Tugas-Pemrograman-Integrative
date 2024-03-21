#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("========================================================")
print("== MENGHITUNG RATA-RATA ANGKA HINGGA -1 AKAN BERHENTI ==")
print("========================================================")

angka_list = []

while True:
    angka = input("Masukkan Angka (-1 untuk berhenti) : ")

    if angka == "-1":
        break

    try:
        angka = float(angka)
        angka_list.append(int(angka))
    except ValueError:
        print("Input harus berupa angka")

if len(angka_list) > 0:
    rata_rata = sum(angka_list) / len(angka_list)
    print("Jumlah Keseluruhannya Adalah : {}".format(sum(angka_list)))
    print("Rata-ratanya adalah : {:.2f}".format(rata_rata))
    print("Angka yang dimasukkan secara berurutan:")
    print('\n'.join(map(str, angka_list)))
else:
    print("Tidak ada angka yang dimasukkan.")
