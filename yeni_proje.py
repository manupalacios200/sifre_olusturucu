import random

harfler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola = int(input("Parolanın uzunluğunu girin:"))
sifre = ""

for i in range(parola):
    sifre += random.choice(harfler)

print("Şifreniz:", sifre)
