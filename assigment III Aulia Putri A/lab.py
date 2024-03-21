#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("======================================================================")
print("== MENGHITUNG DAN MENYIMPAN TINGGI DAN BERAT SESEORANG DALAM METRIK ==")
print("======================================================================")

class BMI_Calculator:
    def __init__(self, berat, tinggi):
        self.berat = berat
        self.tinggi = tinggi

    def BMI_Value(self):
        tinggi_meter = self.tinggi / 100  # Mengonversi tinggi dari cm menjadi meter
        bmi = self.berat / (tinggi_meter ** 2)  # Menghitung BMI menggunakan rumus
        return round(bmi, 2)  # Mengembalikan BMI dengan 2 angka di belakang koma

    def __eq__(self, other):
        if isinstance(other, BMI_Calculator):
            return self.berat == other.berat and self.tinggi == other.tinggi
        return False


# Contoh penggunaan:
if __name__ == "__main__":
    # Masukkan tinggi dan berat Anda dalam satuan metrik
    tinggi_cm = float(input("Masukkan tinggi Anda (cm): "))
    berat_kg = float(input("Masukkan berat Anda (kg): "))

    # Membuat objek kelas BMI_Calculator
    my_bmi_calculator = BMI_Calculator(berat_kg, tinggi_cm)

    # Memanggil metode BMI_Value() untuk mendapatkan nilai BMI
    bmi = my_bmi_calculator.BMI_Value()

    print("BMI Anda adalah:", bmi)  # Menampilkan nilai BMI

    # Contoh penggunaan metode __eq__
    other_bmi_calculator = BMI_Calculator(berat_kg, tinggi_cm)
    if my_bmi_calculator == other_bmi_calculator:
        print("Kedua objek BMI_Calculator memiliki berat dan tinggi yang sama.")
    else:
        print("Kedua objek BMI_Calculator memiliki berat dan/atau tinggi yang berbeda.")
