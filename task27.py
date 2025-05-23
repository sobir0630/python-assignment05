pul = 38500
birliklar = [10000, 5000, 2000, 1000, 500, 100, 50, 10, 1]
natija = []

qolgan = pul
for birlik in birliklar:
    soni = qolgan // birlik
    if soni > 0:
        natija.append(f"{soni} dona {birlik} so‘mlik")
        qolgan %= birlik

print(", ".join(natija))