mapel = ["Matematika", "Informatika", "Bahasa Indonesia"]
mapel.append("Seni Budaya")
print("Daftar mapel:", mapel)
print("Mapel pertama:", mapel[0])
print("Jumlah mapel:", len(mapel))

siswa = {"nama": "Ajeng", "sekolah": "SMKN 2 Subang", "jumlah_buku": 7}
siswa["hobi"] = "membaca"
print("Data siswa:", siswa)
print("Nama:", siswa["nama"])
for kunci, isi in siswa.items():
    print(kunci, "=", isi)
