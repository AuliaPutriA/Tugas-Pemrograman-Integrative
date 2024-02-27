#Nama: Aulia Putri Andini
#NIM: 239902246 (PMM)

print("========================================================")
print("=========== KONVERSI GAJI TAHUNAN KE BULANAN ===========")
print("========================================================")

#Menghitung Gaji Bulanan
def JGT(GajiBulananKaryawan):
    GajiBulananKaryawan = GajiTahunan / 12
    return round(GajiBulananKaryawan)
#round digunakan pembulatan 0 desimal

#data diri
Nama = input("Nama Karyawan : ")
NIK = input("Nomor Identifikasi Karyawan : ")
NOtlp = input("Nomor Telepon : ")
NoREK = input("Nomer Rekening :")
NmBank = input("Nama Bank : ")
GajiTahunan = float(input("Jumlah Gaji Tahunan Anda : Rp "))

#memanggil fungsi 
GajiBulananKaryawan = JGT(GajiTahunan)  

print("=======================================================")
print("=======================================================")

print("\nData Diri :")
print("Nama : ", Nama )
print("NIK : ", NIK)
print("No telepon : ", NOtlp)
print("No Rekening : ", NoREK)
print("Nama Bank : ", NmBank)
print("Jumlah Gaji Tahunan : Rp ", GajiTahunan)
print("Jumlah Gaji Bulanan : Rp ", GajiBulananKaryawan)

