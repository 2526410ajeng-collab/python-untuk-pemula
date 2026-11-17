class Siswa:
    def __init__(self, nama, sekolah, jumlah_buku):
        self.nama = nama
        self.sekolah = sekolah
        self.jumlah_buku = jumlah_buku

    def perkenalan(self):
        return "Nama saya " + self.nama + " dari " + self.sekolah

    def tambah_buku(self, jumlah):
        self.jumlah_buku += jumlah

siswa1 = Siswa("Ajeng", "SMKN 2 Subang", 7)
print(siswa1.perkenalan())
print("Jumlah buku:", siswa1.jumlah_buku)
siswa1.tambah_buku(3)
print("Jumlah buku sekarang:", siswa1.jumlah_buku)
