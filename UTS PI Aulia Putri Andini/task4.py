#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("=============================================================")
print("== Program Menghitung dan Menyimpan Tinggi Badan Seseorang ==")
print("=============================================================")

class BMI_Calculator:
    def __init__(self, berat, tinggi):
        self.berat = berat
        self.tinggi = tinggi

    def BMI_Value(self):
        tinggi_meter = self.tinggi / 100  # Mengonversi tinggi dari cm menjadi meter
        bmi = self.berat / (tinggi_meter ** 2)  # Menghitung BMI menggunakan rumus
        return round(bmi, 2)  # Mengembalikan BMI dengan 2 angka di belakang koma

if __name__ == "__main__":

    # Masukkan tinggi dan berat Anda dalam satuan metrik
    tinggi_kaki = float(input("Masukkan tinggi Anda (kaki): "))
    berat_pon = float(input("Masukkan berat Anda (pon): "))

    # Membuat objek kelas BMI_Calculator
    my_bmi_calculator = BMI_Calculator(berat_pon, tinggi_kaki)

    # Memanggil metode BMI_Value() untuk mendapatkan nilai BMI
    bmi = my_bmi_calculator.BMI_Value()

    print("Tinggi anda adalah (kaki): ", tinggi_kaki)
    print("Berat anda adalah (pon): ", berat_pon)
    print("BMI Anda adalah:", bmi)

    # Contoh perbandingan BMI dua objek
    orang1 = BMI_Calculator(150, 5.5)  # berat dalam pon, tinggi dalam kaki
    orang2 = BMI_Calculator(70, 6)     # berat dalam pon, tinggi dalam kaki

    if orang1 == orang2:
        print("BMI orang1 sama dengan BMI orang2")
    else:
        print("BMI orang1 tidak sama dengan BMI orang2")
