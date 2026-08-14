while True:
    print("Kalkulator ")
    print("1. +")
    print("2. -")
    print("3. x")
    print("4. :")
    print("5. Exit")

    pilih_operasi = int(input("operasi yang dipilih:"))
    if pilih_operasi == 1:
        print("Penjumlahan")
        angka1 = float(input("Masukan angka pertama:"))
        angka2 = float(input("Masukan angka kedua:"))
        print(f"{angka1} + {angka2} = {angka1 + angka2}")
    elif pilih_operasi == 2:
        print("Pengurangan")
        angka1 = float(input("Masukan angka pertama:"))
        angka2 = float(input("Masukan angka kedua:"))
        print(f"{angka1} - {angka2} = {angka1 - angka2}")
    elif pilih_operasi == 3:
        print("Perkalian")
        angka1 = float(input("Masukan angka pertama:"))
        angka2 = float(input("Masukan angka kedua:"))
        print(f" {angka1} x {angka2} = {angka1 * angka2}")
    elif pilih_operasi == 4:
        print("Pembagian")
        angka1 = float(input("Masukan angka pertama:"))
        angka2 = float(input("Masukan angka kedua:"))
        print(f"{angka1} : {angka2} = {angka1 / angka2}")
    elif pilih_operasi == 5:
        print("Keluar dari kalkulator")
        break 
    else:
        print("opsi tidak ditemukan")
        continue
             