tugas = {
    "matematika": "Belajar operasi hitung dasar",
    "fisika": "Latihan soal gaya dan energi",
    "pemrograman": "Membuat program Python"
}

while True:
    print("\n=== Daftar Tugas ===")
    for i, nama_tugas in enumerate(tugas.keys(), start=1):
        print(f"{i}. {nama_tugas}")

    print("\nMenu:")
    print("1. Tambah tugas")
    print("2. Hapus tugas")
    print("3. Buka tugas")
    print("4. Edit tugas")
    print("0. Keluar")

    pilihan = input("Pilih angka: ")

    if pilihan == "0":
        print("Keluar dari program.")
        break
    elif pilihan == "1":
        tugas_baru = input("Masukkan tugas baru: ").strip()
        if tugas_baru:
            if tugas_baru in tugas:
                print("Tugas sudah ada.")
            else:
                tugas[tugas_baru] = "Belum ada deskripsi"
                print(f"'{tugas_baru}' ditambahkan.")
        else:
            print("Nama tugas tidak boleh kosong.")
    elif pilihan == "2":
        tugas_hapus = input("Masukkan nama tugas yang ingin dihapus: ").strip()
        if tugas_hapus in tugas:
            del tugas[tugas_hapus]
            print(f"'{tugas_hapus}' dihapus.")
        else:
            print("Tugas tidak ditemukan.")
    elif pilihan == "3":
        nama_tugas = input("Masukkan nama tugas yang ingin dibuka: ").strip()
        if nama_tugas in tugas:
            print(f"\n=== {nama_tugas.upper()} ===")
            print(tugas[nama_tugas])
            aksi = input("Ketik 'edit' untuk mengubah isi tugas, atau enter untuk kembali: ").strip().lower()
            if aksi == "edit":
                isi_baru = input("Masukkan isi tugas baru: ")
                tugas[nama_tugas] = isi_baru
                print("Isi tugas diperbarui.")
        else:
            print("Tugas tidak ditemukan.")
    elif pilihan == "4":
        nama_tugas = input("Masukkan nama tugas yang ingin diedit: ").strip()
        if nama_tugas in tugas:
            nama_baru = input("Masukkan nama tugas baru: ").strip()
            if nama_baru:
                tugas[nama_baru] = tugas.pop(nama_tugas)
                print(f"Tugas diubah menjadi '{nama_baru}'.")
            else:
                print("Nama tugas tidak boleh kosong.")
        else:
            print("Tugas tidak ditemukan.")
    else:
        print("Pilihan tidak valid, coba lagi.")