print("List tugas pembelajaran")
list_tugas = ["matematika", "fisika", "pemrograman"]
while True:
    for i, nama_tugas in enumerate(list_tugas, start=1):
        print(f"{i}. {nama_tugas}")

    print("\nMenu:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. pilih tugas")
    print("0. Keluar")
    pilih_menu = int(input("Pilih menu: "))

    if pilih_menu == 1:
        tugas_baru = input("tugas apa yang mau ditambahkan?")
        list_tugas.append(tugas_baru)
        print(f" {tugas_baru} Berhasil ditambahkan")
    elif pilih_menu == 2:
        print("daftar tugas yang tersedia:")
        for i, nama_tugas in enumerate(list_tugas, start=1):
            print(f"{i}. {nama_tugas}")
        hapus_tugas = int(input("masukkan nomor tugas yang mau dihapus: ")) - 1
        if 0 <= hapus_tugas < len(list_tugas):
            tugas_dihapus = list_tugas.pop(hapus_tugas)
            print(f"{tugas_dihapus} berhasil dihapus")
        else:
            print("tugas tidak ada dalam list")
            continue
    elif pilih_menu == 3:
        print("daftar tugas yang tersedia:")
        for i, nama_tugas in enumerate(list_tugas, start=1):
            print(f"{i}. {nama_tugas}")
        tugas_yang_dipilih = input("tugas yang mau dipilih?")
        if tugas_yang_dipilih in list_tugas:
            print(f"membuka tugas: {tugas_yang_dipilih}")
        else:
            print(f"tugas {tugas_yang_dipilih}: tidak ada di list tugas")
            continue
    elif pilih_menu == 0:
        print("Keluar dari program.")
        break
    else:
        print("Pilihan tidak valid, coba lagi.")
        continue

    