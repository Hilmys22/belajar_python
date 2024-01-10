# latihan logika dan komperasi

# membuat gabungan area dari angka
inputuser = float(input("\nMasukkan angka\n kurang dari 5\n atau lebih dari 10 = "))

# +++++5-----
# pemeriksa kurang dari 5 = benar
iskurangdari = (inputuser < 5)
print("Kurang dari 5 =", iskurangdari)

# -----10+++++
# pemeriksa lebih dari 10
islebihdari = (inputuser > 10)
print("lebih dari 10 =", islebihdari)

iscorect = iskurangdari or islebihdari
print("angka yang sudah dimasukkan = ", iscorect)


inputuser = float(input("\nMasukkan angka\n kurang dari 5\n atau lebih dari 10 = "))

# -----5+++++
# pemeriksa lebih 5 = benar kurang = salah
islebihdari =(inputuser > 5)
print("lebih dari 5 =", islebihdari)

# +++++10-----
# pemeriksa kurang dari 10 = benar lebih dari = salah

iskurangdari = (inputuser < 10)
print("kurang dari 10 =", iskurangdari)

iscorect = islebihdari and iskurangdari
print ("angka yang sudah dimasukkan =", iscorect)