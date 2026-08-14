while True:
    print("Kalkulator")
    list_operasi = ("+ atau tambah", "- atau kurang", "x atau perkalian", ": atau pembagian", "^ atau pangkat", "EXIT")
    for i, pilih_operasi in enumerate(list_operasi, start=1):
        print(f"Yang bisa dilakukan: {i}. {pilih_operasi}")
    pilihan = int(input("Pilih:"))
    if pilihan == 1:
        angka1 = float(input("Angka pertama:"))
        angka2 = float(input("Angka kedua:"))
        hasil = angka1 + angka2
        print(f"{angka1} + {angka2} hasilnya= {hasil}")
        break 


   
