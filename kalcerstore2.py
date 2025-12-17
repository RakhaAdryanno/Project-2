# KALCER STORE BY TENXI

# inisialisasi produk
hoodie = 599000
pants = 499000
jacket = 799000

print("SELAMAT DATANG DI KALCER STORE BY TENXI\n")
print("Daftar harga:")
print(f"- Hoodie : Rp {hoodie:,}".replace(',', '.'))
print(f"- Pants  : Rp {pants:,}".replace(',', '.'))
print(f"- Jacket : Rp {jacket:,}\n".replace(',', '.'))

# input
pilih_produk = input("Masukkan jenis produk ( hoodie | pants | jacket ): ").lower()
jumlah = int(input("Masukkan jumlah produk: "))

# proses perhitungan
if pilih_produk == "hoodie":
    harga = hoodie
elif pilih_produk == "pants":
    harga = pants
elif pilih_produk == "jacket":
    harga = jacket
else:
    harga = 0
    print("Jenis produk tidak valid!")

# output total harga
if harga > 0:
    total = jumlah * harga
    print("\nRincian Pembelian:")
    print(f"{'Harga per item':<15} : Rp {harga:,}".replace(',', '.'))
    print(f"{'Jumlah dibeli':<15} : {jumlah}")
    print(f"{'Total harga':<15} : Rp {total:,}".replace(',', '.'))
    print("\nGA BAYAR DILEMPAR KE NERAKA!!!!! LMAO ")
