#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("======================================================================")
print("== Program Mencetak jumlah angka dengan pemisah koma dan tiga digit ==")
print("======================================================================")

def format_number(number):
    # Membuat string dari angka dengan pemisah koma setiap tiga digit
    return '{:,}'.format(number)

def main():
    # Membuka file input.txt untuk dibaca
    with open('input.txt', 'r') as file:
        # Membaca semua baris dari file dan menggabungkannya menjadi satu string
        numbers_str = file.read()
    
    # Membuat list dari string angka yang dipisahkan oleh spasi
    numbers = numbers_str.split()
    
    # Menginisialisasi variabel untuk menyimpan jumlah angka
    total = 0
    
    # Menghitung jumlah angka dan mengubahnya menjadi integer
    for num_str in numbers:
        num = int(num_str)
        total += num
    
    # Mencetak jumlah angka dengan format yang diinginkan
    print("Total angka dengan pemisah koma setiap tiga digit:", format_number(total))

if __name__ == "__main__":
    main()
