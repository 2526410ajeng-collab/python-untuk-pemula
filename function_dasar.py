def sapa(nama):
    return "Halo, " + nama

def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar

def total_harga(jumlah, harga=25000):
    return jumlah * harga

print(sapa("Ajeng"))
print("Luas:", luas_persegi_panjang(8, 5))
print("Total harga:", total_harga(7))
print("Total harga diskon:", total_harga(7, 20000))
