profil_kontak = {"nama":"Arthur", "nomor_hp":"085", "kota":"saint_dennis", "hobi":"membantu_orang"}
for key, value in profil_kontak.items():
    print(f"{key}: {value}")

print(profil_kontak["kota"])  
selengkapnya = input("Detail profil kontak")    
print(profil_kontak.get(selengkapnya, "Belum diketahui"))
profil_kontak ["Nama_ayah"] = "Morgan"
print(f"Data baru berhasil ditambahkan: {profil_kontak ["Nama_ayah"]}")