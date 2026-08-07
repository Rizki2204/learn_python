while True:
    print("=== KALKULATOR ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("5. Keluar")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 1:
        angka1 = int(input("Angka pertama: "))
        angka2 = int(input("Angka kedua: "))
        hasil = angka1 + angka2
        print(f"{angka1} + {angka2} = {hasil}")
    elif pilihan == 2:
        angka1 = int(input("Angka pertama: "))
        angka2 = int(input("Angka kedua: "))
        hasil = angka1 - angka2
        print(f"{angka1} - {angka2} = {hasil}")
    elif pilihan == 3:
        angka1 = int(input("Angka pertama: "))
        angka2 = int(input("Angka kedua: "))
        hasil = angka1 * angka2
        print(f"{angka1} * {angka2} = {hasil}")
    elif pilihan == 4:
        angka1 = int(input("Angka pertama: "))
        angka2 = int(input("Angka kedua: "))
        hasil = angka1 / angka2
        print(f"{angka1} / {angka2} = {hasil}")
    elif pilihan == 5:
        print("keluar dari kalkulator, sampai jumpa!")
        break
    else:
        print("belum memilih menu, coba lagi")