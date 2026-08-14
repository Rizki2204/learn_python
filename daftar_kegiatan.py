kegiatan_baru = input("Hari ini apa saja kegiatannya: ")
with open("daftar_kegiatan.txt", "a") as new:
    new.write(kegiatan_baru + "\n")
with open("daftar_kegiatan.txt", "r") as new:
    kegiatan_baru = new.read()
    print(kegiatan_baru)  