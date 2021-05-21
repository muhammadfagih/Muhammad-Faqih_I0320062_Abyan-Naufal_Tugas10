import os

print("")
print("="*50)
x = "Soal 3 : Append ke biodata_diri.txt"
print(x.center(50))
print("="*50)
print("")

nama = input("Masukkan nama : ")
umur = int(input("Masukkan umur : "))
alamat = input("Masukkan alamat : ")
hobi = input("Masukkan hobi :")

teks = f"\n\nNama : {nama}\nUmur : {umur}\nAlamat : {alamat}\nHobi : {hobi}"

file = open("dir/biodata_diri.txt","a")

file.write(teks)

file.close()

print("")
print("="*50)
x = "Selesai"
print(x.center(50))
print("="*50)
print("")