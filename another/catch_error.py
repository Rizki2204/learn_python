try:
    angka1 = float(input("Masukan angka pertama: "))
    angka2 = float(input("Masukan angka kedua: "))
    hasil = angka1 / angka2
except ZeroDivisionError:
     print("Tidak bisa membagi dengan 0")
except ValueError:
     print("Input wajib angka!")
else:
     print(f"Input valid! Hasilnya = {hasil}")
finally:
     print("Perhitungan selesai!")           
               