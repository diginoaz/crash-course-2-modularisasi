"""
program menghitung luas segitiga
luas_segitiga = alas * tinggi / 2
"""

print('Menghitung laus segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f"luas segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga} meter persegi")

print('\nMenghitung laus segitiga 2 denan copy paste')
alas = 20
tinggi = 8
luas_segitiga = alas * tinggi / 2
print(f"luas segitiga dengan alas = {alas} dan tinggi = {tinggi} memiliki luas = {luas_segitiga} meter persegi")


print('\nMembuat fungsi menghitung_luas_segitiga')
def menghitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

print(f"Menghitung luas segitiga dengan fungsi, hasilnya = {menghitung_luas_segitiga(10, 6)}")
print(f"Menghitung luas segitiga dengan fungsi, hasilnya = {menghitung_luas_segitiga(20, 2)}")
print(f"Menghitung luas segitiga dengan fungsi, hasilnya = {menghitung_luas_segitiga(100, 3)}")
